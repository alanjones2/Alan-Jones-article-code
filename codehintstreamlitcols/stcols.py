import streamlit as st

st.markdown("<h1 style='color:blue'> Customizing Streamlit Columns</h1>", unsafe_allow_html=True)

st.write("""Streamlit does not have a very sophisticated page layout model 
and that to a great extent is an advantage as it makes constructing apps simple.
However,sometime you want to do a bit more...
""")

st.header("1. Two columns without padding")
st.info("_Here are two columns of text - what if you would like more separation between them?_")
col1, col2 = st.columns(2)

with col1:
    st.write("""
To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
""")

with col2:
    st.write("""
And by opposing end them. To die—to sleep,
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to: 'tis a consummation
    """)

st.header("2. Two columns with padding")
st.info("_Here are the two columns again, try adjusting the padding with the dropdown menu, below_")
p = st.selectbox("Adjust the padding:",(1,2,3,4,5))
col1, pad, col2 = st.columns((10,p,10))

with col1:
    st.write("""
Devoutly to be wish'd. To die, to sleep;
To sleep, perchance to dream—ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
""")

with col2:
    st.write("""
Must give us pause—there's the respect
That makes calamity of so long life.
For who would bear the whips and scorns of time,
Th'oppressor's wrong, the proud man's contumely,
""")

st.header("3. One narrow centred column")
st.info("_Adjust the width of a centred column_")
p = st.selectbox("Adjust the margins:",(1,2,3,4,5))
cpad1, col, pad2 = st.columns((p,10,p))

with col:
    st.write("""
Devoutly to be wish'd. To die, to sleep;
To sleep, perchance to dream—ay, there's the rub:
For in that sleep of death what dreams may come,
When we have shuffled off this mortal coil,
""")

st.header("4. Calculate the number of columns")
st.info("_How about deciding on the number of columns you need dynamically. Select the number of coulumns below._")

numCols = st.selectbox("Number of columns:",(1,2,3))

quotes = [
    """The pangs of dispriz'd love, the law's delay,
The insolence of office, and the spurns
That patient merit of th'unworthy takes,
When he himself might his quietus make
With a bare bodkin? Who would fardels bear,
""",
"""To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscovere'd country, from whose bourn
No traveller returns, puzzles the will,
And makes us rather bear those ills we have
Than fly to others that we know not of?

""",
"""Thus conscience doth make cowards of us all,
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry
And lose the name of action.
"""]
cols = st.columns(numCols)

for c in range(numCols):
    with cols[c]:
        st.write(quotes[c])


st.markdown("<div style='font-size:small;text-align:right'><i>Text from William Shakespeare's play Hamlet, Act 3, Scene 1</i></div>",unsafe_allow_html=True)