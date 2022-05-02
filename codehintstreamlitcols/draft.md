## Code hints: Streamlit 
#  Customizing Streamlit Columns
## Streamlit has a limited layout model and this is normally an advantage as it allows the simple construction of sophisticated apps. But sometimes you want to modify the layout.

![](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/codehintstreamlitcols/images/Screenshot%202022-05-02%20163012.png)

Streamlit provides us with pretty good UI controls and options that allow the easy creation of sophisticated and great-looking apps.

But sometimes you want to do something a little different.

This short article I'll show you a handful of code hints that you can use to adjust the padding and width of columns and how to set the number of columns dynamically - a technique that you could use to displays columns of data from a downloaded file when you are not sure how many columns there will be.

### Padding columns

The standard way to use columns in Streamlit is like this:

    st.header("1. Two columns without padding")
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

But sometimes the columns are too close together and a little padding between them helps. So what we can do is add a blank column between them.

    st.header("2. Two columns with padding")
    col1, padding, col2 = st.columns((10,2,10))

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

### Centering a column

Similarly, we can use outer padding for a centred column.



    st.header("3. One narrow centred column")
    cpad1, col, pad2 = st.columns((10,10,10))

    with col:
        st.write("""
        Devoutly to be wish'd. To die, to sleep;
        To sleep, perchance to dream—ay, there's the rub:
        For in that sleep of death what dreams may come,
        When we have shuffled off this mortal coil,
        """)

### Dynamically displaying columns 

Another thing we can do is decide on the number of columns dynamically by using an list to hold the number of columns that we want.

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

As you can see above, we record the number of columns in a list. Then, in a loop, we write text in each of those columns.

This is all quite straightforward stuff but hopefully useful.

Please feel free to copy this code and modify it for your own purposes. You find the source code to an interactive demo in my [Github repo](https://github.com/alanjones2/Alan-Jones-article-code/tree/master/codehintstreamlitcols.

And you can find a Streamlit app that demonstrates all the techniques in the [Streamlit Cloud](https://share.streamlit.io/alanjones2/alan-jones-article-code/codehintstreamlitcols/stcols.py).

---

As always, thanks for reading. If you'd like to see other articles please take a look at my [web page](https://alanjones2.github.io/) and/or subscribe to my occasional newsletter [Technofile](https://technofile.substack.com/).