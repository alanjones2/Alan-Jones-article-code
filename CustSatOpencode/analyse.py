"""Rebuild the StepSavvy report using only Python's standard library."""

import csv
import hashlib
import json
import re
from collections import Counter
from datetime import date
from html import escape
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "data" / "shoes.md"

# Analyst-assigned themes, keyed by product and source review number.
# Anchors make changes to the evidence fail visibly rather than silently reusing codes.
ANNOTATIONS = {
    "CloudStrider Sneakers": [
        ("sole started to peel", ["Durability"], ["Initial comfort"]),
        ("way too tight", ["Sizing / fit"], []),
        ("hold onto odors", ["Odour retention"], ["Short-run performance"]),
        ("lightweight and breathable", [], ["Lightweight / breathable"]),
    ],
    "PeakTrek Hikers": [
        ("feet were soaked", ["Waterproofing"], []),
        ("don’t grip well", ["Wet-surface grip"], []),
        ("padding was thicker", ["Padding / comfort"], ["Sturdiness / ankle support"]),
        ("No blisters", [], ["Comfort", "Sturdiness"]),
    ],
    "SwiftShine Heels": [
        ("heel broke", ["Heel integrity"], []),
        ("scratches so easily", ["Finish durability"], ["Appearance"]),
        ("pain after an hour", ["Comfort"], []),
        ("on your feet all day", ["Prolonged-wear comfort"], ["Appearance"]),
    ],
    "LuxeLace Oxfords": [
        ("held up beautifully", [], ["Material quality", "Durability"]),
        ("more color options", ["Colour choice"], ["Style", "Comfort"]),
        ("Great craftsmanship", [], ["Comfort", "Craftsmanship"]),
        ("stiff out of the box", ["Initial stiffness"], ["Comfort after break-in", "Style"]),
    ],
    "EcoStep Slip-Ons": [
        ("recycled materials", [], ["Ease of wear", "Sustainable materials"]),
        ("rainy weather", ["Rain suitability"], ["Comfort", "Style"]),
        ("Lightweight, breathable", [], ["Lightweight / breathable", "Sustainable materials"]),
        ("more arch support", ["Arch support"], ["Fit", "Sustainable design"]),
    ],
    "BounceMax Runners": [
        ("even after 10 miles", [], ["Cushioning", "Long-distance comfort"]),
        ("support and bounce", [], ["Support", "Cushioning"]),
        ("slightly bulkier", ["Bulk / weight"], ["Performance", "Comfort"]),
        ("Durable, comfortable", [], ["Durability", "Comfort", "Style"]),
    ],
}


def parse_source(text):
    retailer_match = re.search(r"### Retailer Name:\s*\*\*(.+?)\*\*", text)
    if not retailer_match or "### Customer feedback" not in text:
        raise ValueError("Missing retailer or feedback section")
    lineup, feedback = text.split("### Customer feedback", 1)
    products = dict(re.findall(r"^\d+\. \*\*(.+?)\*\* - (.+)$", lineup, re.M))
    blocks = re.findall(r"^### \*\*(.+?)\*\*\s*(.*?)(?=^### \*\*|\Z)", feedback, re.M | re.S)
    if not products or len(blocks) != len(products) or {name for name, _ in blocks} != set(products):
        raise ValueError("Product lineup and feedback sections do not match")
    if set(products) != set(ANNOTATIONS):
        raise ValueError("Product lineup has changed; review the qualitative annotations")
    reviews = []
    for name, block in blocks:
        matches = re.findall(r'(\d+)\. \*Rating: (\d+)/5\*\s*\*"(.*?)"\*', block, re.S)
        if len(matches) != len(re.findall(r"Rating:", block)) or not matches:
            raise ValueError(f"Unparsed review in {name}")
        if len(matches) != len(ANNOTATIONS[name]):
            raise ValueError(f"Review count changed for {name}; update annotations")
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        for index, ((number, rating, comment), (anchor, concerns, strengths)) in enumerate(
            zip(matches, ANNOTATIONS[name]), 1
        ):
            if int(number) != index or not 1 <= int(rating) <= 5 or anchor not in comment:
                raise ValueError(f"Review {number} for {name} changed; check evidence and annotations")
            reviews.append({
                "review_id": f"{slug}-{index}", "product": name,
                "review_number": index, "rating": int(rating), "comment": comment.strip(),
                "concerns": concerns, "strengths": strengths,
            })
    return retailer_match.group(1), products, reviews


def summarise(products, reviews):
    summaries = []
    for product, description in products.items():
        group = [review for review in reviews if review["product"] == product]
        ratings = [review["rating"] for review in group]
        positive = sum(rating >= 4 for rating in ratings)
        low = sum(rating <= 2 for rating in ratings)
        summaries.append({
            "product": product, "description": description, "review_count": len(group),
            "average_rating": mean(ratings), "positive_count": positive,
            "positive_percent": positive / len(group) * 100,
            "low_count": low, "low_percent": low / len(group) * 100,
            "neutral_count": ratings.count(3),
            "rating_distribution": {str(rating): ratings.count(rating) for rating in range(1, 6)},
            "concern_mentions": dict(Counter(theme for review in group for theme in review["concerns"])),
        })
    summaries.sort(key=lambda item: (-item["average_rating"], item["product"]))
    for item in summaries:
        item["rank"] = 1 + sum(other["average_rating"] > item["average_rating"] for other in summaries)
    return summaries


def make_chart(summaries):
    height = 115 + 64 * len(summaries)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {height}" role="img" aria-labelledby="chart-title chart-desc">',
             '<title id="chart-title">Average customer rating by product</title>',
             '<desc id="chart-desc">Ranked average ratings on a zero-to-five scale. ' +
             escape("; ".join(f'{s["product"]}: {s["average_rating"]:.2f} out of 5, {s["review_count"]} reviews' for s in summaries)) + '</desc>',
             '<rect width="900" height="100%" fill="#ffffff"/>',
             '<g font-family="system-ui, sans-serif" font-size="16" fill="#243649">']
    for tick in range(6):
        x = 255 + tick * 100
        parts.append(f'<line x1="{x}" y1="35" x2="{x}" y2="{height-55}" stroke="#e5eaf0"/>')
        parts.append(f'<text x="{x}" y="{height-28}" text-anchor="middle">{tick}</text>')
    for index, item in enumerate(summaries):
        y = 48 + index * 64
        colour = "#087f8c" if item["average_rating"] >= 4 else "#b65920"
        parts.extend([
            f'<text x="240" y="{y+22}" text-anchor="end">{escape(item["product"])}</text>',
            f'<rect x="255" y="{y}" width="{item["average_rating"]*100}" height="34" rx="5" fill="{colour}"/>',
            f'<text x="{265+item["average_rating"]*100}" y="{y+22}" font-weight="700">{item["average_rating"]:.2f}</text>',
            f'<text x="815" y="{y+22}" font-size="14">n = {item["review_count"]}</text>',
        ])
    parts.append(f'<text x="505" y="{height-3}" text-anchor="middle" font-size="14">Average rating (out of 5)</text></g></svg>')
    return "\n".join(parts)


def cite(product, number, label=None):
    slug = re.sub(r"[^a-z0-9]+", "-", product.lower()).strip("-")
    return f'<a href="#{slug}-{number}">{escape(label or f"review {number}")}</a>'


def make_report(retailer, summaries, reviews, chart, digest):
    overall = mean(review["rating"] for review in reviews)
    positive = sum(review["rating"] >= 4 for review in reviews)
    low = sum(review["rating"] <= 2 for review in reviews)
    lookup = {item["product"]: item for item in summaries}
    rows = "".join(
        f'<tr><td>{s["rank"]}</td><th scope="row">{escape(s["product"])}</th>'
        f'<td>{s["average_rating"]:.2f}</td><td>{s["review_count"]}</td>'
        f'<td>{s["positive_count"]}/{s["review_count"]} ({s["positive_percent"]:.0f}%)</td>'
        f'<td>{s["low_count"]}/{s["review_count"]} ({s["low_percent"]:.0f}%)</td></tr>' for s in summaries
    )
    cards = []
    for product in ("SwiftShine Heels", "CloudStrider Sneakers", "PeakTrek Hikers"):
        item = lookup[product]
        evidence = "".join(
            f'<li>{escape(", ".join(review["concerns"]))} — '
            f'{cite(product, review["review_number"], str(review["rating"]) + "/5, review " + str(review["review_number"]))}: '
            f'<q>{escape(review["comment"])}</q></li>'
            for review in reviews if review["product"] == product and review["concerns"]
        )
        interpretations = {
            "SwiftShine Heels": "Appearance is a strength in two comments, but comfort is qualified or criticised in two. One review reports a broken heel and one reports finish damage. These experiences conflict with the comfort positioning and suggest investigating structural reliability and wear comfort first.",
            "CloudStrider Sneakers": "Lightness and breathability receive praise, while separate reviews describe sole separation, a tight fit and odour retention. Initial comfort does not establish long-term durability. Fit guidance and construction quality are the clearest areas to investigate.",
            "PeakTrek Hikers": "The two low-rated comments challenge waterproofing and wet-surface grip, while the higher-rated comments praise sturdiness and support. This mixed evidence warrants testing performance under the conditions described rather than assuming every pair has the same problem.",
        }
        cards.append(f'<article class="product-card"><h3>{escape(product)} <span>{item["average_rating"]:.2f}/5</span></h3>'
                     f'<p>{escape(interpretations[product])}</p><ul class="evidence">{evidence}</ul></article>')
    appendix = []
    for item in summaries:
        entries = []
        for review in reviews:
            if review["product"] != item["product"]:
                continue
            tags = "; ".join(review["concerns"]) or "None coded"
            strengths = "; ".join(review["strengths"]) or "None coded"
            entries.append(f'<li id="{review["review_id"]}"><strong>Review {review["review_number"]} · {review["rating"]}/5</strong>'
                           f'<blockquote>{escape(review["comment"])}</blockquote>'
                           f'<p class="small">Concerns: {escape(tags)}. Strengths: {escape(strengths)}.</p></li>')
        appendix.append(f'<h3>{escape(item["product"])}</h3><p class="small">{escape(item["description"])}</p><ol class="reviews">{"".join(entries)}</ol>')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="StepSavvy customer satisfaction analysis of 24 supplied product reviews.">
<title>{escape(retailer)} | Customer satisfaction report</title>
<style>
:root {{color-scheme:light;--ink:#203247;--muted:#526174;--teal:#087f8c;--line:#dce4eb}}
* {{box-sizing:border-box}} body {{margin:0;background:#f3f6f9;color:var(--ink);font:16px/1.65 system-ui,-apple-system,sans-serif}}
main {{max-width:1120px;margin:0 auto;padding:32px 28px 64px}} header {{background:#153549;color:white;padding:42px;border-radius:16px}}
h1 {{font-size:clamp(2rem,5vw,3.1rem);line-height:1.15;margin:8px 0 18px}} h2 {{font-size:1.6rem;margin:0 0 18px}} h3 {{font-size:1.15rem}}
header p {{max-width:760px;color:#dfebf0}} .eyebrow {{font-size:.8rem;letter-spacing:.13em;text-transform:uppercase;font-weight:700}}
nav {{display:flex;flex-wrap:wrap;gap:20px;margin:22px 0}} a {{color:#096b83;text-underline-offset:3px}} a:focus-visible {{outline:3px solid #b65920}}
section {{background:white;border:1px solid var(--line);border-radius:12px;padding:28px;margin:24px 0}}
.metrics {{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:24px 0}} .metric {{padding:20px;background:white;border:1px solid var(--line);border-radius:12px}}
.metric strong {{display:block;font-size:2rem;color:var(--teal)}} .metric span,.small,figcaption {{font-size:.9rem;color:var(--muted)}}
.callout {{border-left:4px solid var(--teal);background:#edf7f8;padding:16px 20px}} .table-wrap {{overflow-x:auto}}
table {{width:100%;border-collapse:collapse;font-size:.95rem}} caption {{text-align:left;color:var(--muted);margin-bottom:12px}}
th,td {{padding:12px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}} thead {{background:#f2f6f8}}
figure {{margin:0}} svg {{width:100%;height:auto;display:block}} .product-card {{border-top:1px solid var(--line);padding:12px 0}}
.product-card h3 {{display:flex;justify-content:space-between;gap:12px}} .product-card h3 span {{color:#a44c18;white-space:nowrap}}
li {{margin:8px 0}} q {{font-style:italic}} .evidence {{padding-left:22px}} blockquote {{margin:8px 0;padding:8px 18px;border-left:3px solid var(--line)}}
.reviews {{padding-left:26px}} .reviews li {{padding:8px 0;scroll-margin-top:24px}} footer {{font-size:.85rem;color:var(--muted)}} code {{overflow-wrap:anywhere}}
@media(max-width:700px) {{main {{padding:16px}} header,section {{padding:22px}} .metrics {{grid-template-columns:repeat(2,1fr)}} table {{min-width:650px}}}}
@media print {{body {{background:white;font-size:11pt}} main {{padding:0;max-width:none}} header {{background:white;color:var(--ink);padding:20px 0}} header p {{color:var(--muted)}} nav {{display:none}} section {{border:0;padding:12px 0}} .metric {{padding:10px}} h2,h3 {{break-after:avoid}} tr,blockquote,.metric {{break-inside:avoid}} a {{color:inherit}}}}
</style>
</head>
<body><main>
<header><div class="eyebrow">{escape(retailer)} · Customer experience insight</div>
<h1>Customer satisfaction report</h1>
<p>A product-level review of satisfaction, reported pain points and practical improvement priorities for the supplied shoe range.</p>
<p class="eyebrow">Prepared {date.today().isoformat()} · 6 products · 24 reviews · Review dates unavailable</p></header>
<nav aria-label="Report sections"><a href="#summary">Executive summary</a><a href="#rankings">Rankings</a><a href="#diagnosis">Performance drivers</a><a href="#actions">Action plan</a><a href="#method">Methodology</a><a href="#evidence">Review evidence</a></nav>
<div class="metrics" aria-label="Portfolio measures">
<div class="metric"><strong>{overall:.2f}/5</strong><span>Mean across supplied reviews</span></div>
<div class="metric"><strong>{positive/len(reviews)*100:.1f}%</strong><span>Positive: {positive}/{len(reviews)} rated 4–5</span></div>
<div class="metric"><strong>{low/len(reviews)*100:.1f}%</strong><span>Low: {low}/{len(reviews)} rated 1–2</span></div>
<div class="metric"><strong>4</strong><span>Reviews per product</span></div></div>
<section id="summary"><h2>Executive summary</h2>
<p><strong>BounceMax Runners leads at 4.75/5; SwiftShine Heels ranks lowest at 2.50/5.</strong> LuxeLace Oxfords and EcoStep Slip-Ons share second place at 4.50/5. All supplied reviews for these three leading products are positive.</p>
<p>PeakTrek Hikers (3.00/5), CloudStrider Sneakers (2.75/5) and SwiftShine Heels (2.50/5) each have two low ratings out of four. Together they account for all six low-rated reviews. Their combined mean is 2.75/5, compared with 4.58/5 for the three leading products.</p>
<p>Prioritise investigation of reported heel breakage and wet-surface grip, then durability, fit and waterproofing. Preserve the comfort and quality strengths of the leading products while checking their smaller concerns.</p>
<div class="callout"><strong>Decision context:</strong> These rankings describe this small supplied review set. With only four reviews per product and no sampling or sales information, they are directional signals, not population satisfaction estimates or proof of defects.</div></section>
<section id="rankings"><h2>Product satisfaction rankings</h2>
<figure>{chart}<figcaption>Average ratings on a fixed 0–5 scale. Labels show exact means and sample sizes; ties share a rank. The table provides the same comparison in text.</figcaption></figure>
<div class="table-wrap"><table><caption>Positive = 4–5 stars; low = 1–2 stars; 3 stars is neutral.</caption>
<thead><tr><th scope="col">Rank</th><th scope="col">Product</th><th scope="col">Mean /5</th><th scope="col">Reviews</th><th scope="col">Positive</th><th scope="col">Low</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="small">There are two neutral reviews: CloudStrider review 3 and SwiftShine review 2. A mean rating is not a percentage of satisfied customers.</p></section>
<section id="diagnosis"><h2>What is driving weaker performance?</h2>
<p>Below, each quoted issue is traceable to its original review. Theme counts refer to comments mentioning a topic, not verified defect rates.</p>{''.join(cards)}
<h3>Strengths and smaller opportunities in the leaders</h3>
<ul><li><strong>BounceMax Runners:</strong> cushioning, support and comfort are recurring strengths. One reviewer notes bulk ({cite('BounceMax Runners',3)}). Evaluate a lighter design only if comfort and support can be retained.</li>
<li><strong>LuxeLace Oxfords:</strong> leather quality, craftsmanship and comfort receive praise. Broader colour choice ({cite('LuxeLace Oxfords',2)}) and initial stiffness ({cite('LuxeLace Oxfords',4)}) are incremental opportunities.</li>
<li><strong>EcoStep Slip-Ons:</strong> convenience, comfort and sustainable materials/design are valued. Rain suitability ({cite('EcoStep Slip-Ons',2)}) and arch support ({cite('EcoStep Slip-Ons',4)}) merit clearer use guidance and evaluation.</li></ul></section>
<section id="actions"><h2>Prioritised action plan</h2>
<p>Suggested timing and ownership are planning recommendations. Confirm priorities using returns, complaint records and product testing; revenue, cost and exposure data were not supplied.</p>
<div class="table-wrap"><table><caption>Operational recommendations linked to the supplied evidence</caption>
<thead><tr><th scope="col">Priority / timing</th><th scope="col">Action and evidence</th><th scope="col">Suggested owner</th><th scope="col">Follow-up measure</th></tr></thead><tbody>
<tr><td><strong>P1 · 0–2 weeks</strong></td><td>Investigate SwiftShine heel integrity and PeakTrek wet-surface grip. Inspect returned pairs, trace batches and reproduce the reported conditions. Evidence: {cite('SwiftShine Heels',1,'broken heel')} and {cite('PeakTrek Hikers',2,'slipping')}.</td><td>Product quality + suppliers</td><td>Document test outcomes and affected batches; establish complaint counts per 100 pairs sold and monitor after any fix.</td></tr>
<tr><td><strong>P2 · 2–6 weeks</strong></td><td>Test CloudStrider sole bonding and size consistency; assess PeakTrek waterproofing against the advertised claim. Update size guidance or product claims where checks support changes. Evidence: {cite('CloudStrider Sneakers',1,'sole peeling')}, {cite('CloudStrider Sneakers',2,'tight sizing')}, {cite('PeakTrek Hikers',1,'water ingress')}.</td><td>Quality assurance + merchandising</td><td>Record test pass rates against agreed specifications; track durability, size-related and water-ingress return rates using sales denominators.</td></tr>
<tr><td><strong>P2 · 2–6 weeks</strong></td><td>Run extended-wear trials for SwiftShine comfort and finish durability, CloudStrider odour retention and PeakTrek padding. Evidence: SwiftShine {cite('SwiftShine Heels',2)}–{cite('SwiftShine Heels',4)}, CloudStrider {cite('CloudStrider Sneakers',3)}, PeakTrek {cite('PeakTrek Hikers',3)}.</td><td>Product development</td><td>Use defined wear durations and conditions; record comfort scores, visible wear and odour results before and after revisions.</td></tr>
<tr><td><strong>P3 · 6–12 weeks</strong></td><td>Protect leading-product comfort and quality; assess BounceMax bulk, LuxeLace colour range/break-in guidance and EcoStep arch support/rain guidance. Validate demand and economics before investing.</td><td>Merchandising + product development</td><td>Gather a larger review sample, compare attribute feedback and pilot costs, and confirm core comfort scores are maintained.</td></tr>
<tr><td><strong>Ongoing · start now</strong></td><td>Collect consistent post-purchase ratings with purchase dates, use conditions, variant/size and return reasons. Review trends by product and batch monthly.</td><td>Customer experience + analytics</td><td>Track review response rate, sample size, 4–5-star share, 1–2-star share and issue-specific return rates. Set improvement targets after a representative baseline is available.</td></tr>
</tbody></table></div></section>
<section id="method"><h2>Methodology and limitations</h2>
<ul><li><strong>Source:</strong> <code>data/shoes.md</code>; all six listed products and 24 reviews are included. No external evidence was added. Four reviews are supplied for each product.</li>
<li><strong>Calculations:</strong> mean = sum of ratings ÷ review count; positive share = count rated 4 or 5 ÷ count; low share = count rated 1 or 2 ÷ count. Three-star reviews are neutral. Portfolio mean weights each review equally. Ranks use unrounded means and competition ranking (1, 2, 2, 4…). Percentages and means are rounded only for display.</li>
<li><strong>Qualitative coding:</strong> concerns and strengths were assigned manually to each comment and are included in the evidence appendix and exported data. A review can contain both; a concern in a 4-star review does not make that review low-rated. Themes describe reported experiences, not established root causes. There was no independent second coder.</li>
<li><strong>Uncertainty:</strong> the selection method, review dates, sales volumes, purchaser verification and customer characteristics are unknown. Selection bias and differing use conditions may affect comparisons. One review is 25% of a product sample; a one-star change in one review changes that product’s mean by 0.25. The 0.25-point lead over the joint runners-up should not be treated as statistically established superiority.</li>
<li><strong>Scope:</strong> no trend, financial impact, defect prevalence or causal inference can be established from these comments alone. Recommendations identify what to investigate; product testing and broader feedback are needed to substantiate causes and measure improvements.</li></ul></section>
<section id="evidence"><h2>Appendix: source reviews and coding</h2><p>Original comments are reproduced below. Review numbers follow their order within each product in the source.</p>{''.join(appendix)}</section>
<footer>Generated by <code>analyse.py</code> from <code>data/shoes.md</code>. Source SHA-256: <code>{digest}</code>. This file includes its chart and styling and works offline.</footer>
</main></body></html>'''


def write_csv(path, records, fields):
    with path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for record in records:
            writer.writerow({key: "; ".join(value) if isinstance(value, list) else value
                             for key, value in record.items()})


def main():
    raw = SOURCE.read_bytes()
    retailer, products, reviews = parse_source(raw.decode("utf-8"))
    summaries = summarise(products, reviews)
    digest = hashlib.sha256(raw).hexdigest()
    reports = ROOT / "reports"
    reports.mkdir(exist_ok=True)
    chart = make_chart(summaries)
    report = make_report(retailer, summaries, reviews, chart, digest)
    (reports / "customer_satisfaction_report.html").write_text(report, encoding="utf-8")
    (reports / "satisfaction_chart.svg").write_text(chart, encoding="utf-8")
    write_csv(ROOT / "data" / "reviews.csv", reviews,
              ["review_id", "product", "review_number", "rating", "comment", "concerns", "strengths"])
    write_csv(ROOT / "data" / "product_summary.csv", summaries,
              ["rank", "product", "description", "review_count", "average_rating", "positive_count",
               "positive_percent", "low_count", "low_percent", "neutral_count"])
    analysis = {
        "retailer": retailer, "source": "data/shoes.md", "source_sha256": digest,
        "generated_on": date.today().isoformat(),
        "method": {"positive_ratings": [4, 5], "low_ratings": [1, 2], "neutral_rating": 3,
                   "themes": "Manual analyst coding; multiple themes permitted per comment"},
        "overall": {"review_count": len(reviews), "product_count": len(products),
                    "average_rating": mean(review["rating"] for review in reviews),
                    "positive_count": sum(review["rating"] >= 4 for review in reviews),
                    "low_count": sum(review["rating"] <= 2 for review in reviews),
                    "neutral_count": sum(review["rating"] == 3 for review in reviews)},
        "products": summaries, "reviews": reviews,
    }
    (ROOT / "data" / "analysis.json").write_text(json.dumps(analysis, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated report for {retailer}: {len(reviews)} reviews, {len(products)} products.")
    for item in summaries:
        print(f'{item["rank"]}. {item["product"]}: {item["average_rating"]:.2f}/5')
    print(f"Report: {reports / 'customer_satisfaction_report.html'}")


if __name__ == "__main__":
    main()
