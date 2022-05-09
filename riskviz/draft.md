# Visualizing Health Risk

## The press can get it wrong when dealing with health risk data. Can visualizations help.

In November 2015, the International Agency for Research in Cancer (part of the World Health Organisation) reported that eating 50 grams of processed meat - bacon or sausages, for example - was associated with an 18% increase in the risk of bowel cancer. 

The press duly reported this scary sounding increase but did not make it clear that this was a _relative_ risk rather than an _absolute_ one.

The sensational headline '__X Gives You Cancer__' may be hard to resist for some newspapers when presented with new medical research data. But sometimes the media get it wrong because the data is misinterpreted by journalists who don't necessarily understand what they have been presented with.

The risk of getting bowel cancer, in the population as a whole, is about 6%. An increase of 18% means that the risk rise to about 7%. 

    6 * 1.18 = 7.08


So, in absolute terms the risk rises by 1% - a much less scary number which is less likely to put people off an occasional English Breakfast or bacon sandwich.

So as not to confuse the public with statistics and percentages that might be misinterpreted, a visualization might help.

I'm going to write some Python code to look at how we might do this. If you want to follow along you'll need to import these libraries.

    import random
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd

Here is some code that constructs a dataframe that represents 100 people and the number of them that will get cancer.

    data = pd.DataFrame()
    pop = 100                   # total population
    chance = 6                  # number who get cancer by chance
    bacon = int(6 * 0.18)       # number who get cancer by eating bacon
    none = pop - chance - bacon # number who won't get cancer 

    data['Non-sufferer'] = [none]
    data['Sufferer by Chance'] = [chance]
    data['Bacon Eater'] = [bacon]

The code mentions bacon to represent processed meat.

First I'm going to draw some bar charts to see if that better represnts the risk of eating bacon. I'll use the plotting features of Pandas to do this.

The following bar chart puts the additional risk into better perspective than the raw data. The  _Bacon Eater_ column is tiny compared to the overall population.

    data.plot.bar(figsize=(8,5))

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/riskviz/images/barv.png)

Would it be better as a stacked chart?

    data.plot.bar(stacked=True,figsize=(8,5))


![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/riskviz/images/barvstacked.png)


The numbers are the same, of course, but the top layer of the bar is not very visible.

What if we were to turn them round so that become horizontal bars.

    data.plot.barh(figsize=(8,5))

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/riskviz/images/barh.png)

    data.plot.barh(stacked=True,figsize=(8,5))

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/riskviz/images/barhstacked.png)


Or perhaps we should try a different sort of chart altogether.

    data.T.plot.pie(subplots=True,figsize=(8,5))

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/riskviz/images/pie.png)

Sometimes pie chart are not at all clear, particulary when there are several categories to represent. However, this one has only 3 different bits of data tp plot and does a pretty good job of showing the releative proportions.

I've used the default color scheme for each of these charts - it might be better to change the colours to hilight the smaller number of Bacon Eaters.

But let's look at something quite different - heat maps.

For this I'm going to use the Seaborn data visualization package. First, though, the data needs to be represented differently. I'm going to construct a 10 by 10 grid with each cell representing someone who is cancer free, who contracts the disease by chance, or who succumbs to too much bacon.

I start by making 3 

    # Arrays of the different cases
    a1 = [0]*data['Non-sufferer'].values[0]
    a2 = [1]*data['Sufferer by Chance'].values[0]
    a3 = [2]*data['Bacon Eater'].values[0]

    # Stitch them together
    a1.extend(a2)
    a1.extend(a3)



![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/riskviz/images/iconarray.png)