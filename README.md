# Distance-on-a-sphere
 ### The Haversine Formula
 
The Earth is round but big, so we can consider it flat for short distances. But, even though the circumference of the Earth is about 40,000 kilometers, flat-Earth formulas for calculating the distance between two points start showing noticeable errors when the distance is more than about 20 kilometers. Therefore, calculating distances on a sphere needs to consider spherical geometry, the study of shapes on the surface of a sphere. 

Spherical geometry considers spherical trigonometry which deals with relationships between trigonometric functions to calculate the sides and angles of spherical polygons. These spherical polygons are defined by a number of intersecting great circles on a sphere. Some rules found in spherical geometry include:

- There are no parallel lines.
- Straight lines are great circles, so any two lines meet in two points.
- The angle between two lines is the angle between the planes of the corresponding great circles.
## The Haversine
Did you know that there are more than the 3 trigonometric functions we are all familiar with sine, cosine and, tangent? These additional trigonometric functions are now obsolete, however, in the past, they were worth naming. 

The additional trigonometric functions are versine, haversine, coversine, hacoversine, exsecant, and excosecant. All of these can be expressed simply in terms of the more familiar trigonometric functions.
### For example, ` haversine(θ) = sin²(θ/2) `

The haversine formula is a very accurate way of computing distances between two points on the surface of a sphere using the latitude and longitude of the two points. The haversine formula is a re-formulation of the spherical law of cosines, but the formulation in terms of haversines is more useful for small angles and distances.

One of the primary applications of trigonometry was navigation, and certain commonly used navigational formulas are stated most simply in terms of these archaic function names. But you might ask, why not just simplify everything down to sines and cosines? The functions listed above were from a time without calculators, or efficient computer processors, when the user calculated angles and direction by hand using log tables, every named function took appreciable effort to evaluate. The point of these functions is if a table simply combines two common operations into one function, it probably made navigational calculations on a rocking ship more efficient.

These function names have a simple naming pattern and in this example, the "Ha" in "Haversine" stands for "half versed sine" where ` haversin(θ) = versin(θ)/2 `

![image not found](Distance-on-a-sphere/3d dist.png)

#### Haversine Formula 
The Haversine formula is perhaps the first equation to consider when understanding how to calculate distances on a sphere. The word "Haversine" comes from the function:
`haversine(θ) = sin²(θ/2)`
The following equation where φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km) is how we translate the above formula to include latitude and longitude coordinates. Note that angles need to be in radians to pass to trig functions:
`a = sin²(φB - φA/2) + cos φA * cos φB * sin²(λB - λA/2)
c = 2 * atan2( √a, √(1−a) )
d = R ⋅ c`

Thanks 
[article](https://community.esri.com/groups/coordinate-reference-systems/blog/2017/10/05/haversine-formula)

