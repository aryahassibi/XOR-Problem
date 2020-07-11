# XOR Problem
XOR problem solved using the [three-layer neural network](https://github.com/aryahassibi/Three-layer-Neural-Network-Using-Matrix#three-layer-neural-network--using-matrix-) that I had made previously
and visualized using the Pygame library.

## *What is main.py?*
In main.py I trained the neural network to solve XOR problem and when you run the program it shows you the result:

     XOR [0, 0]  ≈  0.09681844789560402
     XOR [1, 0]  ≈  0.8642830639305592
     XOR [1, 1]  ≈  0.16421678094863154
     XOR [0, 1]  ≈  0.8545802569550945
     
     
> *note:* for more information read the comments inside the code or read about it over [here](https://github.com/aryahassibi/Three-layer-Neural-Network-Using-Matrix#three-layer-neural-network--using-matrix-).

## *What is Visualize.py?*
Visualize.py shows the learning process of the neural network visually. <br>
the neural network predicts a color for each cell based on its coordinate.
![XORGIF](https://user-images.githubusercontent.com/31355913/87221857-8d2f2d00-c384-11ea-9f45-1be7fbeb804c.gif)

> *note:* white pixels represent **true** and black cells represent **correct**
<br>

> Pygame coordinate system:<br>

  |   |Left|Right|
  |:---:|:---:|:---:|
  |**Up**|(0, 0)|(1, 0)|
  |**Down**|(0, 1)|(1, 1)|




> *note:* you can read about the other files [here](https://github.com/aryahassibi/Three-layer-Neural-Network-Using-Matrix#three-layer-neural-network--using-matrix-).
