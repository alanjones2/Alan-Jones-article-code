### Statisitics 101

## Mean, Median and Mode: What Are they and When Should You Use Them

### You probably remember Mean, Median and Mode from high school stats classes but they are often used wrongly. We look at how you _should_ use them with Python Pandas examples.

What is the average height of an 18-year-old American male? Or the average price of a house in Madrid? Or the average grade achieved by high school students in England?

These are all perfectly worded questions but mean something slightly different in each case. The average in the first case is calculated using the _mean_, the house prices would be better represented using the _median_ and the school grades by the _mode_.

The average is a measurement of a central tendency and typically we would expect that it would be calculated by adding a set of values  together and then dividing by the number of values. This is the _mean_ and this works perfectly well for a normally distributed set of data like height.

You can legitimately track the height of adult Americans by adding all of their height together and divided by the number of Americans. (That's quite a task so you'd probably want to take a representative sample instead.)

And if you tracked this over time you'd get a graph like the one below from Our World in Data.


![Change in height](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/meanmedianmode/images/changeinheight.png)

This works fine because height follows a normal distribution as illustrated here:

![Height distribution](https://github.com/alanjones2/Alan-Jones-article-code/raw/master/meanmedianmode/images/heightnormaldist.jpg)

Licensed by [Illustrative Mathematics](https://illustrativemathematics.org/) under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International 

In a normal distribution values are distributed evenly around a central point and tail off similarly to the left and right. You can see the mean in the graph above is 70 inches.




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Player Name</th>
      <th>Weekly Wage</th>
      <th>Yearly Salary</th>
      <th>Age</th>
      <th>Position</th>
      <th>Nationality</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>José Campaña</td>
      <td>33000</td>
      <td>1716000</td>
      <td>28.0</td>
      <td>DM, AM C</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>José Morales</td>
      <td>28000</td>
      <td>1456000</td>
      <td>33.0</td>
      <td>AM RL, ST</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Aitor Fernández</td>
      <td>25000</td>
      <td>1300000</td>
      <td>30.0</td>
      <td>GK</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Enis Bardhi</td>
      <td>25000</td>
      <td>1300000</td>
      <td>26.0</td>
      <td>AM LC</td>
      <td>North Macedonia</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Coke</td>
      <td>24000</td>
      <td>1248000</td>
      <td>34.0</td>
      <td>D RC, M R</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Shkodran Mustafi</td>
      <td>19000</td>
      <td>988000</td>
      <td>29.0</td>
      <td>D C</td>
      <td>Germany</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Nikola Vukčević</td>
      <td>19000</td>
      <td>988000</td>
      <td>29.0</td>
      <td>DM</td>
      <td>Montenegro</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Carlos Clerc</td>
      <td>18000</td>
      <td>936000</td>
      <td>29.0</td>
      <td>D/WB L</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Rúben Vezo</td>
      <td>18000</td>
      <td>936000</td>
      <td>27.0</td>
      <td>D C</td>
      <td>Portugal</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Dani Gómez</td>
      <td>18000</td>
      <td>936000</td>
      <td>22.0</td>
      <td>ST</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Gonzalo Melero</td>
      <td>17000</td>
      <td>884000</td>
      <td>27.0</td>
      <td>DM, AM C</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Nemanja Radoja</td>
      <td>16000</td>
      <td>832000</td>
      <td>28.0</td>
      <td>DM</td>
      <td>Serbia</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Hernâni</td>
      <td>15000</td>
      <td>780000</td>
      <td>29.0</td>
      <td>AM RL</td>
      <td>Portugal</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Roger Martí</td>
      <td>15000</td>
      <td>780000</td>
      <td>30.0</td>
      <td>ST</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Dani Cárdenas</td>
      <td>14000</td>
      <td>728000</td>
      <td>24.0</td>
      <td>GK</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Jorge De Frutos</td>
      <td>14000</td>
      <td>728000</td>
      <td>24.0</td>
      <td>AM RL</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Roberto Soldado</td>
      <td>14000</td>
      <td>728000</td>
      <td>36.0</td>
      <td>ST</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Enric Franquesa</td>
      <td>13000</td>
      <td>676000</td>
      <td>24.0</td>
      <td>D/WB/M L</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Jorge Miramón</td>
      <td>11000</td>
      <td>572000</td>
      <td>32.0</td>
      <td>D/WB/AM R</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Oscar Duarte</td>
      <td>10000</td>
      <td>520000</td>
      <td>32.0</td>
      <td>D C</td>
      <td>Costa Rica</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Mickaël Malsa</td>
      <td>10000</td>
      <td>520000</td>
      <td>25.0</td>
      <td>DM</td>
      <td>Martinique</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Son</td>
      <td>9000</td>
      <td>468000</td>
      <td>27.0</td>
      <td>D/WB/AM R</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Pablo Martínez</td>
      <td>9000</td>
      <td>468000</td>
      <td>23.0</td>
      <td>AM LC</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Róber Pier</td>
      <td>8700</td>
      <td>452400</td>
      <td>26.0</td>
      <td>D C, DM</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Sergio Postigo</td>
      <td>8000</td>
      <td>416000</td>
      <td>32.0</td>
      <td>D RC</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Pepelu</td>
      <td>7800</td>
      <td>405600</td>
      <td>22.0</td>
      <td>DM</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Álex Blesa</td>
      <td>2000</td>
      <td>104000</td>
      <td>19.0</td>
      <td>DM, AM C</td>
      <td>Spain</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Álex Cantero</td>
      <td>2000</td>
      <td>104000</td>
      <td>21.0</td>
      <td>AM RL, ST</td>
      <td>Spain</td>
    </tr>
  </tbody>
</table>
</div>



The data comes from the web site [Salary Sport](https://salarysport.com/football/la-liga/levante/)

    Mean weekly wage with Messi 49051.724137931036
    Mean weekly wage without Messi 15089.285714285714
    3.250765149969394
    

https://gist.github.com/alanjones2/4d570fc1c9835d4732c1d64bbaaca547

    Median weekly wage with Messi 15000.0
    Median weekly wage without Messi 14500.0
    1.0344827586206897
    
