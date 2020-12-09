# Choregraphe bezier export in Python.
from naoqi import ALProxy



def elephant(srv) :
    motion = srv["motion"]
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.24, 2.32, 3.72, 4.8, 6.12, 7.16])
    keys.append([[0.637045, [3, -0.426667, 0], [3, 0.36, 0]], [0.149268, [3, -0.36, 0], [3, 0.466667, 0]], [0.637045, [3, -0.466667, 0], [3, 0.36, 0]], [0.149268, [3, -0.36, 0], [3, 0.44, 0]], [0.637045, [3, -0.44, 0], [3, 0.346667, 0]], [-0.208621, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([1.24, 2.32, 3.72, 4.8, 6.12, 7.16])
    keys.append([[-0.3735, [3, -0.426667, 0], [3, 0.36, 0]], [-0.370809, [3, -0.36, 0], [3, 0.466667, 0]], [-0.3735, [3, -0.466667, 0], [3, 0.36, 0]], [-0.370809, [3, -0.36, 0], [3, 0.44, 0]], [-0.3735, [3, -0.44, 0], [3, 0.346667, 0]], [-0.00460196, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("HipPitch")
    times.append([0.96, 2.04, 3.44, 4.52, 5.84, 7.16])
    keys.append([[-0.941134, [3, -0.333333, 0], [3, 0.36, 0]], [-0.0407854, [3, -0.36, 0], [3, 0.466667, 0]], [-0.941134, [3, -0.466667, 0], [3, 0.36, 0]], [-0.0407854, [3, -0.36, 0], [3, 0.44, 0]], [-0.941134, [3, -0.44, 0], [3, 0.44, 0]], [-0.0352817, [3, -0.44, 0], [3, 0, 0]]])

    names.append("HipRoll")
    times.append([0.96, 2.04, 3.44, 4.52, 5.84, 7.16])
    keys.append([[-0.00218318, [3, -0.333333, 0], [3, 0.36, 0]], [-0.00218318, [3, -0.36, 0], [3, 0.466667, 0]], [-0.00218318, [3, -0.466667, 0], [3, 0.36, 0]], [-0.00218318, [3, -0.36, 0], [3, 0.44, 0]], [-0.00218318, [3, -0.44, 0], [3, 0.44, 0]], [-0.00766992, [3, -0.44, 0], [3, 0, 0]]])

    names.append("KneePitch")
    times.append([0.96, 2.04, 3.44, 4.52, 5.84, 7.16])
    keys.append([[0.353169, [3, -0.333333, 0], [3, 0.36, 0]], [-0.00319533, [3, -0.36, 0], [3, 0.466667, 0]], [0.353169, [3, -0.466667, 0], [3, 0.36, 0]], [-0.00319533, [3, -0.36, 0], [3, 0.44, 0]], [0.353169, [3, -0.44, 0], [3, 0.44, 0]], [-0.00766992, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([1.24, 2.32, 3.72, 4.8, 6.12, 7.16])
    keys.append([[-1.56207, [3, -0.426667, 0], [3, 0.36, 0]], [-1.54741, [3, -0.36, 0], [3, 0.466667, 0]], [-1.56207, [3, -0.466667, 0], [3, 0.36, 0]], [-1.54741, [3, -0.36, 0], [3, 0.44, 0]], [-1.56207, [3, -0.44, 0], [3, 0.346667, 0]], [-0.515418, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([1.24, 2.32, 3.72, 4.8, 6.12, 7.16])
    keys.append([[0, [3, -0.426667, 0], [3, 0.36, 0]], [0.0280028, [3, -0.36, 0], [3, 0.466667, 0]], [0, [3, -0.466667, 0], [3, 0.36, 0]], [0.0280028, [3, -0.36, 0], [3, 0.44, 0]], [0, [3, -0.44, 0.0280028], [3, 0.346667, -0.0220628]], [-1.23792, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([1.24, 2.32, 3.72, 4.8, 6.12, 7.16])
    keys.append([[0.602755, [3, -0.426667, 0], [3, 0.36, 0]], [0.602755, [3, -0.36, 0], [3, 0.466667, 0]], [0.602755, [3, -0.466667, 0], [3, 0.36, 0]], [0.602755, [3, -0.36, 0], [3, 0.44, 0]], [0.602755, [3, -0.44, 0], [3, 0.346667, 0]], [0.589631, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([1.24, 2.32, 3.72, 4.8, 6.12, 7.16])
    keys.append([[-0.403171, [3, -0.426667, 0], [3, 0.36, 0]], [-0.654399, [3, -0.36, 0], [3, 0.466667, 0]], [-0.403171, [3, -0.466667, 0], [3, 0.36, 0]], [-0.654399, [3, -0.36, 0], [3, 0.44, 0]], [-0.403171, [3, -0.44, -0.251228], [3, 0.346667, 0.197937]], [1.55699, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([1.24, 2.32, 3.72, 4.8, 6.12, 7.16])
    keys.append([[0.139697, [3, -0.426667, 0], [3, 0.36, 0]], [0.15506, [3, -0.36, 0], [3, 0.466667, 0]], [0.139697, [3, -0.466667, 0], [3, 0.36, 0]], [0.15506, [3, -0.36, 0], [3, 0.44, 0]], [0.139697, [3, -0.44, 0.00517175], [3, 0.346667, -0.00407471]], [0.127321, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([1.24, 2.32, 3.72, 4.8, 6.12, 7.16])
    keys.append([[0, [3, -0.426667, 0], [3, 0.36, 0]], [0, [3, -0.36, 0], [3, 0.466667, 0]], [0, [3, -0.466667, 0], [3, 0.36, 0]], [0, [3, -0.36, 0], [3, 0.44, 0]], [0, [3, -0.44, 0], [3, 0.346667, 0]], [0.0106959, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([1.24, 1.8, 2.84, 3.72, 4.28, 5.32, 6.12, 7.16])
    keys.append([[0.534071, [3, -0.426667, 0], [3, 0.186667, 0]], [0.00872665, [3, -0.186667, 0], [3, 0.346667, 0]], [0.884857, [3, -0.346667, 0], [3, 0.293333, 0]], [0.534071, [3, -0.293333, 0.178471], [3, 0.186667, -0.113573]], [0.00872665, [3, -0.186667, 0], [3, 0.346667, 0]], [0.884857, [3, -0.346667, 0], [3, 0.266667, 0]], [0.534071, [3, -0.266667, 0.0037283], [3, 0.346667, -0.00484679]], [0.529224, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([1.24, 2.32, 3.72, 4.8, 6.12, 7.16])
    keys.append([[1.2363, [3, -0.426667, 0], [3, 0.36, 0]], [1.24098, [3, -0.36, 0], [3, 0.466667, 0]], [1.2363, [3, -0.466667, 0], [3, 0.36, 0]], [1.24098, [3, -0.36, 0], [3, 0.44, 0]], [1.2363, [3, -0.44, 0.00114215], [3, 0.346667, -0.000899875]], [1.23486, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([1.76, 2.84, 4.24, 5.32, 7.16])
    keys.append([[0.602465, [3, -0.6, 0], [3, 0.36, 0]], [0.98, [3, -0.36, 0], [3, 0.466667, 0]], [0.602465, [3, -0.466667, 0], [3, 0.36, 0]], [0.98, [3, -0.36, 0], [3, 0.613333, 0]], [0.599297, [3, -0.613333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([1.24, 2.32, 3.72, 4.8, 6.12, 7.16])
    keys.append([[0.53058, [3, -0.426667, 0], [3, 0.36, 0]], [-0.506132, [3, -0.36, 0], [3, 0.466667, 0]], [0.53058, [3, -0.466667, 0], [3, 0.36, 0]], [-0.506132, [3, -0.36, 0], [3, 0.44, 0]], [0.53058, [3, -0.44, -0.384078], [3, 0.346667, 0.302607]], [1.55392, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([1.24, 2.32, 3.72, 4.8, 6.12, 7.16])
    keys.append([[-0.00872665, [3, -0.426667, 0], [3, 0.36, 0]], [-0.0383779, [3, -0.36, 0], [3, 0.466667, 0]], [-0.00872665, [3, -0.466667, 0], [3, 0.36, 0]], [-0.0383779, [3, -0.36, 0], [3, 0.44, 0]], [-0.00872665, [3, -0.44, 0], [3, 0.346667, 0]], [-0.13499, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([1.24, 2.32, 3.72, 4.8, 6.12, 7.16])
    keys.append([[-1.27409, [3, -0.426667, 0], [3, 0.36, 0]], [-1.27223, [3, -0.36, 0], [3, 0.466667, 0]], [-1.27409, [3, -0.466667, 0], [3, 0.36, 0]], [-1.27223, [3, -0.36, 0], [3, 0.44, 0]], [-1.27409, [3, -0.44, 0], [3, 0.346667, 0]], [-0.019984, [3, -0.346667, 0], [3, 0, 0]]])
    motion.angleInterpolationBezier(names, times, keys)



def disco(srv) :


    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.16, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
    keys.append([[-0.476475, [3, -0.52, 0], [3, 0.28, 0]], [0.338594, [3, -0.28, 0], [3, 0.32, 0]], [-0.476475, [3, -0.32, 0], [3, 0.28, 0]], [0.338594, [3, -0.28, 0], [3, 0.306667, 0]], [-0.476475, [3, -0.306667, 0], [3, 0.28, 0]], [0.338594, [3, -0.28, 0], [3, 0.32, 0]], [-0.476475, [3, -0.32, 0], [3, 0.28, 0]], [0.338594, [3, -0.28, 0], [3, 0.146667, 0]], [0.0680678, [3, -0.146667, 0.106735], [3, 0.226667, -0.164954]], [-0.476475, [3, -0.226667, 0], [3, 0.28, 0]], [0.338594, [3, -0.28, 0], [3, 0.32, 0]], [-0.476475, [3, -0.32, 0], [3, 0.28, 0]], [0.338594, [3, -0.28, 0], [3, 0.306667, 0]], [-0.476475, [3, -0.306667, 0], [3, 0.28, 0]], [0.338594, [3, -0.28, 0], [3, 0.32, 0]], [-0.476475, [3, -0.32, 0], [3, 0.28, 0]], [0.338594, [3, -0.28, 0], [3, 0.4, 0]], [-0.17185, [3, -0.4, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.16, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
    keys.append([[-0.745256, [3, -0.52, 0], [3, 0.28, 0]], [0.0411095, [3, -0.28, 0], [3, 0.32, 0]], [-0.745256, [3, -0.32, 0], [3, 0.28, 0]], [0.0411095, [3, -0.28, 0], [3, 0.306667, 0]], [-0.745256, [3, -0.306667, 0], [3, 0.28, 0]], [0.018508, [3, -0.28, 0], [3, 0.32, 0]], [-0.745256, [3, -0.32, 0], [3, 0.28, 0]], [0.289725, [3, -0.28, -0.256143], [3, 0.146667, 0.13417]], [0.425684, [3, -0.146667, -0.0596529], [3, 0.226667, 0.0921908]], [0.745256, [3, -0.226667, 0], [3, 0.28, 0]], [-0.0411095, [3, -0.28, 0], [3, 0.32, 0]], [0.745256, [3, -0.32, 0], [3, 0.28, 0]], [-0.0411095, [3, -0.28, 0], [3, 0.306667, 0]], [0.745256, [3, -0.306667, 0], [3, 0.28, 0]], [-0.018508, [3, -0.28, 0], [3, 0.32, 0]], [0.745256, [3, -0.32, 0], [3, 0.28, 0]], [-0.289725, [3, -0.28, 0], [3, 0.4, 0]], [0.00916195, [3, -0.4, 0], [3, 0, 0]]])

    names.append("HipPitch")
    times.append([0.72, 1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
    keys.append([[-0.376033, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.036954, [3, -0.266667, 0], [3, 0.28, 0]], [-0.344024, [3, -0.28, 0], [3, 0.32, 0]], [-0.0404086, [3, -0.32, 0], [3, 0.28, 0]], [-0.339835, [3, -0.28, 0], [3, 0.306667, 0]], [-0.038321, [3, -0.306667, 0], [3, 0.28, 0]], [-0.341769, [3, -0.28, 0], [3, 0.32, 0]], [-0.0367355, [3, -0.32, 0], [3, 0.28, 0]], [-0.34817, [3, -0.28, 0], [3, 0.373333, 0]], [-0.035085, [3, -0.373333, 0], [3, 0.28, 0]], [-0.341769, [3, -0.28, 0], [3, 0.32, 0]], [-0.0382761, [3, -0.32, 0], [3, 0.28, 0]], [-0.339629, [3, -0.28, 0], [3, 0.306667, 0]], [-0.0396041, [3, -0.306667, 0], [3, 0.28, 0]], [-0.341605, [3, -0.28, 0], [3, 0.32, 0]], [-0.0362713, [3, -0.32, 0], [3, 0.28, 0]], [-0.343065, [3, -0.28, 0], [3, 0.4, 0]], [-0.0495279, [3, -0.4, 0], [3, 0, 0]]])

    names.append("HipRoll")
    times.append([1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
    keys.append([[0, [3, -0.52, 0], [3, 0.28, 0]], [0, [3, -0.28, 0], [3, 0.32, 0]], [0, [3, -0.32, 0], [3, 0.28, 0]], [0, [3, -0.28, 0], [3, 0.306667, 0]], [0, [3, -0.306667, 0], [3, 0.28, 0]], [0, [3, -0.28, 0], [3, 0.32, 0]], [0, [3, -0.32, 0], [3, 0.28, 0]], [0, [3, -0.28, 0], [3, 0.373333, 0]], [0, [3, -0.373333, 0], [3, 0.28, 0]], [0, [3, -0.28, 0], [3, 0.32, 0]], [0, [3, -0.32, 0], [3, 0.28, 0]], [0, [3, -0.28, 0], [3, 0.306667, 0]], [0, [3, -0.306667, 0], [3, 0.28, 0]], [0, [3, -0.28, 0], [3, 0.32, 0]], [0, [3, -0.32, 0], [3, 0.28, 0]], [0, [3, -0.28, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0, 0]]])

    names.append("KneePitch")
    times.append([0.72, 1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
    keys.append([[0.166965, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.00379234, [3, -0.266667, 0], [3, 0.28, 0]], [0.185949, [3, -0.28, 0], [3, 0.32, 0]], [-0.0129339, [3, -0.32, 0], [3, 0.28, 0]], [0.180821, [3, -0.28, 0], [3, 0.306667, 0]], [-0.00320919, [3, -0.306667, 0], [3, 0.28, 0]], [0.187035, [3, -0.28, 0], [3, 0.32, 0]], [-0.00931236, [3, -0.32, 0], [3, 0.28, 0]], [0.182162, [3, -0.28, 0], [3, 0.373333, 0]], [-0.0111253, [3, -0.373333, 0], [3, 0.28, 0]], [0.187035, [3, -0.28, 0], [3, 0.32, 0]], [-0.00683206, [3, -0.32, 0], [3, 0.28, 0]], [0.184441, [3, -0.28, 0], [3, 0.306667, 0]], [-0.0119436, [3, -0.306667, 0], [3, 0.28, 0]], [0.179202, [3, -0.28, 0], [3, 0.32, 0]], [-0.0114876, [3, -0.32, 0], [3, 0.28, 0]], [0.187691, [3, -0.28, 0], [3, 0.4, 0]], [-0.013167, [3, -0.4, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.68, 1.04, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.12, 8.48, 8.8, 9.2, 9.64, 10.12, 10.6, 11, 11.44, 11.92, 12.36, 12.76, 13.2, 13.68, 14.16, 14.56, 15, 15.6, 16.2, 16.4])
    keys.append([[-1.37289, [3, -0.24, 0], [3, 0.12, 0]], [-1.12923, [3, -0.12, -0.150485], [3, 0.146667, 0.183927]], [-0.369652, [3, -0.146667, -0.0875841], [3, 0.28, 0.167206]], [-0.202446, [3, -0.28, 0], [3, 0.32, 0]], [-0.369652, [3, -0.32, 0], [3, 0.28, 0]], [-0.202446, [3, -0.28, 0], [3, 0.306667, 0]], [-0.369652, [3, -0.306667, 0], [3, 0.28, 0]], [-0.202446, [3, -0.28, 0], [3, 0.32, 0]], [-0.369652, [3, -0.32, 0], [3, 0.28, 0]], [-0.202446, [3, -0.28, 0], [3, 0.146667, 0]], [-0.820305, [3, -0.146667, 0], [3, 0.12, 0]], [-0.23305, [3, -0.12, -0.106817], [3, 0.106667, 0.0949484]], [-0.138102, [3, -0.106667, 0], [3, 0.133333, 0]], [-1.309, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.257754, [3, -0.146667, 0], [3, 0.16, 0]], [-1.4591, [3, -0.16, 0], [3, 0.16, 0]], [-0.138102, [3, -0.16, 0], [3, 0.133333, 0]], [-1.309, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.257754, [3, -0.146667, 0], [3, 0.16, 0]], [-1.4591, [3, -0.16, 0], [3, 0.146667, 0]], [-0.138102, [3, -0.146667, 0], [3, 0.133333, 0]], [-1.309, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.257754, [3, -0.146667, 0], [3, 0.16, 0]], [-1.4591, [3, -0.16, 0], [3, 0.16, 0]], [-0.138102, [3, -0.16, 0], [3, 0.133333, 0]], [-1.309, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.257754, [3, -0.146667, 0], [3, 0.2, 0]], [-0.984366, [3, -0.2, 0], [3, 0.2, 0]], [-0.513992, [3, -0.2, -0.139872], [3, 0.0666667, 0.0466242]], [-0.424876, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.68, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.12, 8.48, 8.8, 9.2, 9.64, 10.12, 10.6, 11, 11.44, 11.92, 12.36, 12.76, 13.2, 13.68, 14.16, 14.56, 15, 15.6, 16.2, 16.4])
    keys.append([[-0.65506, [3, -0.24, 0], [3, 0.266667, 0]], [-0.380475, [3, -0.266667, 0], [3, 0.28, 0]], [-0.618244, [3, -0.28, 0], [3, 0.32, 0]], [-0.380475, [3, -0.32, 0], [3, 0.28, 0]], [-0.618244, [3, -0.28, 0], [3, 0.306667, 0]], [-0.380475, [3, -0.306667, 0], [3, 0.28, 0]], [-0.618244, [3, -0.28, 0], [3, 0.32, 0]], [-0.380475, [3, -0.32, 0], [3, 0.28, 0]], [-0.618244, [3, -0.28, 0], [3, 0.146667, 0]], [0.410152, [3, -0.146667, -0.263362], [3, 0.12, 0.215478]], [0.818273, [3, -0.12, -0.0372809], [3, 0.106667, 0.0331386]], [0.851412, [3, -0.106667, 0], [3, 0.133333, 0]], [0.0750492, [3, -0.133333, 0.0667938], [3, 0.146667, -0.0734732]], [0.00157596, [3, -0.146667, 0], [3, 0.16, 0]], [0.460767, [3, -0.16, -0.141639], [3, 0.16, 0.141639]], [0.851412, [3, -0.16, 0], [3, 0.133333, 0]], [0.0750492, [3, -0.133333, 0.0667938], [3, 0.146667, -0.0734732]], [0.00157596, [3, -0.146667, 0], [3, 0.16, 0]], [0.460767, [3, -0.16, -0.147798], [3, 0.146667, 0.135481]], [0.851412, [3, -0.146667, 0], [3, 0.133333, 0]], [0.0750492, [3, -0.133333, 0.0667938], [3, 0.146667, -0.0734732]], [0.00157596, [3, -0.146667, 0], [3, 0.16, 0]], [0.460767, [3, -0.16, -0.141639], [3, 0.16, 0.141639]], [0.851412, [3, -0.16, 0], [3, 0.133333, 0]], [0.0750492, [3, -0.133333, 0.0667938], [3, 0.146667, -0.0734732]], [0.00157596, [3, -0.146667, 0.0734732], [3, 0.2, -0.100191]], [-1.34565, [3, -0.2, 0], [3, 0.2, 0]], [-1.22484, [3, -0.2, -0.0338201], [3, 0.0666667, 0.0112734]], [-1.21037, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.68, 1.04, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.48, 8.8, 9.2, 9.64, 10.12, 10.6, 11, 11.44, 11.92, 12.36, 12.76, 13.2, 13.68, 14.16, 14.56, 15, 15.6, 16.2, 16.4])
    keys.append([[0.2, [3, -0.24, 0], [3, 0.12, 0]], [0.6, [3, -0.12, 0], [3, 0.146667, 0]], [0.2648, [3, -0.146667, 0.000419055], [3, 0.28, -0.000800013]], [0.264, [3, -0.28, 0], [3, 0.32, 0]], [0.2648, [3, -0.32, 0], [3, 0.28, 0]], [0.264, [3, -0.28, 0], [3, 0.306667, 0]], [0.2648, [3, -0.306667, 0], [3, 0.28, 0]], [0.264, [3, -0.28, 0], [3, 0.32, 0]], [0.2648, [3, -0.32, 0], [3, 0.28, 0]], [0.264, [3, -0.28, 0], [3, 0.266667, 0]], [0.663802, [3, -0.266667, -0.158095], [3, 0.106667, 0.0632381]], [0.928, [3, -0.106667, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0.142794], [3, 0.146667, -0.157073]], [0.0283999, [3, -0.146667, 0], [3, 0.16, 0]], [0.75, [3, -0.16, -0.149933], [3, 0.16, 0.149933]], [0.928, [3, -0.16, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0.142794], [3, 0.146667, -0.157073]], [0.0283999, [3, -0.146667, 0], [3, 0.16, 0]], [0.75, [3, -0.16, -0.156452], [3, 0.146667, 0.143415]], [0.928, [3, -0.146667, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0.142794], [3, 0.146667, -0.157073]], [0.0283999, [3, -0.146667, 0], [3, 0.16, 0]], [0.75, [3, -0.16, -0.149933], [3, 0.16, 0.149933]], [0.928, [3, -0.16, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0], [3, 0.146667, 0]], [0.5284, [3, -0.146667, -0.0897482], [3, 0.2, 0.122384]], [0.936396, [3, -0.2, -0.013951], [3, 0.2, 0.013951]], [0.950347, [3, -0.2, 0], [3, 0.0666667, 0]], [0.2968, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.68, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.12, 8.48, 8.8, 9.64, 10.6, 11.44, 12.36, 13.2, 14.16, 15, 16.4])
    keys.append([[0.97784, [3, -0.24, 0], [3, 0.266667, 0]], [1.29573, [3, -0.266667, -0.0694014], [3, 0.28, 0.0728715]], [1.40466, [3, -0.28, 0], [3, 0.32, 0]], [1.29573, [3, -0.32, 0], [3, 0.28, 0]], [1.40466, [3, -0.28, 0], [3, 0.306667, 0]], [1.29573, [3, -0.306667, 0], [3, 0.28, 0]], [1.40466, [3, -0.28, 0], [3, 0.32, 0]], [1.29573, [3, -0.32, 0], [3, 0.28, 0]], [1.40466, [3, -0.28, 0], [3, 0.146667, 0]], [0.172788, [3, -0.146667, 0.449845], [3, 0.12, -0.368055]], [-1.04904, [3, -0.12, 0.160692], [3, 0.106667, -0.142838]], [-1.19188, [3, -0.106667, 0], [3, 0.28, 0]], [0.995607, [3, -0.28, 0], [3, 0.32, 0]], [-1.19188, [3, -0.32, 0], [3, 0.28, 0]], [0.995607, [3, -0.28, 0], [3, 0.306667, 0]], [-1.19188, [3, -0.306667, 0], [3, 0.28, 0]], [0.995607, [3, -0.28, 0], [3, 0.32, 0]], [-1.19188, [3, -0.32, 0], [3, 0.28, 0]], [0.995607, [3, -0.28, -0.285274], [3, 0.466667, 0.475457]], [1.47106, [3, -0.466667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.68, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.48, 8.8, 9.2, 9.64, 10.12, 10.6, 11, 11.44, 11.92, 12.36, 12.76, 13.2, 13.68, 14.16, 14.56, 15, 15.6, 16.2])
    keys.append([[0.500047, [3, -0.24, 0], [3, 0.266667, 0]], [0.401871, [3, -0.266667, 0.0234467], [3, 0.28, -0.0246191]], [0.35585, [3, -0.28, 0], [3, 0.32, 0]], [0.401871, [3, -0.32, 0], [3, 0.28, 0]], [0.35585, [3, -0.28, 0], [3, 0.306667, 0]], [0.401871, [3, -0.306667, 0], [3, 0.28, 0]], [0.35585, [3, -0.28, 0], [3, 0.32, 0]], [0.401871, [3, -0.32, 0], [3, 0.28, 0]], [0.35585, [3, -0.28, 0], [3, 0.266667, 0]], [0.886453, [3, -0.266667, -0.145388], [3, 0.106667, 0.0581554]], [0.966481, [3, -0.106667, -0.0513879], [3, 0.133333, 0.0642349]], [1.23332, [3, -0.133333, 0], [3, 0.146667, 0]], [0.324005, [3, -0.146667, 0], [3, 0.16, 0]], [1.23332, [3, -0.16, 0], [3, 0.16, 0]], [0.966481, [3, -0.16, 0], [3, 0.133333, 0]], [1.23332, [3, -0.133333, 0], [3, 0.146667, 0]], [0.324005, [3, -0.146667, 0], [3, 0.16, 0]], [1.23332, [3, -0.16, 0], [3, 0.146667, 0]], [0.966481, [3, -0.146667, 0], [3, 0.133333, 0]], [1.23332, [3, -0.133333, 0], [3, 0.146667, 0]], [0.324005, [3, -0.146667, 0], [3, 0.16, 0]], [1.23332, [3, -0.16, 0], [3, 0.16, 0]], [0.966481, [3, -0.16, 0], [3, 0.133333, 0]], [1.23332, [3, -0.133333, 0], [3, 0.146667, 0]], [0.324005, [3, -0.146667, 0], [3, 0.2, 0]], [0.407503, [3, -0.2, 0], [3, 0.2, 0]], [0.146991, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.68, 1.04, 1.48, 2.32, 3.28, 4.12, 5.04, 5.88, 6.84, 7.68, 8.48, 8.8, 9.64, 10.6, 11.44, 12.36, 13.2, 14.16, 15, 16.2, 16.4])
    keys.append([[0.11961, [3, -0.24, 0], [3, 0.12, 0]], [-0.289725, [3, -0.12, 0.0773137], [3, 0.146667, -0.0944945]], [-0.395814, [3, -0.146667, 0.0128558], [3, 0.28, -0.0245428]], [-0.420357, [3, -0.28, 0], [3, 0.32, 0]], [-0.395814, [3, -0.32, 0], [3, 0.28, 0]], [-0.420357, [3, -0.28, 0], [3, 0.306667, 0]], [-0.395814, [3, -0.306667, 0], [3, 0.28, 0]], [-0.420357, [3, -0.28, 0], [3, 0.32, 0]], [-0.395814, [3, -0.32, 0], [3, 0.28, 0]], [-0.420357, [3, -0.28, 0], [3, 0.266667, 0]], [-0.122946, [3, -0.266667, -0.0390195], [3, 0.106667, 0.0156078]], [-0.107338, [3, -0.106667, 0], [3, 0.28, 0]], [-0.400331, [3, -0.28, 0], [3, 0.32, 0]], [-0.107338, [3, -0.32, 0], [3, 0.28, 0]], [-0.400331, [3, -0.28, 0], [3, 0.306667, 0]], [-0.107338, [3, -0.306667, 0], [3, 0.28, 0]], [-0.400331, [3, -0.28, 0], [3, 0.32, 0]], [-0.107338, [3, -0.32, 0], [3, 0.28, 0]], [-0.400331, [3, -0.28, 0], [3, 0.4, 0]], [0.000370312, [3, -0.4, -0.138036], [3, 0.0666667, 0.023006]], [0.0827939, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.72, 1.08, 1.52, 1.92, 2.36, 2.84, 3.32, 3.72, 4.16, 4.64, 5.08, 5.48, 5.92, 6.4, 6.88, 7.28, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 15.64, 16.24, 16.44])
    keys.append([[1.34689, [3, -0.253333, 0], [3, 0.12, 0]], [1.1205, [3, -0.12, 0.181319], [3, 0.146667, -0.221612]], [0.138102, [3, -0.146667, 0], [3, 0.133333, 0]], [1.309, [3, -0.133333, 0], [3, 0.146667, 0]], [0.257754, [3, -0.146667, 0], [3, 0.16, 0]], [1.4591, [3, -0.16, 0], [3, 0.16, 0]], [0.138102, [3, -0.16, 0], [3, 0.133333, 0]], [1.309, [3, -0.133333, 0], [3, 0.146667, 0]], [0.257754, [3, -0.146667, 0], [3, 0.16, 0]], [1.4591, [3, -0.16, 0], [3, 0.146667, 0]], [0.138102, [3, -0.146667, 0], [3, 0.133333, 0]], [1.309, [3, -0.133333, 0], [3, 0.146667, 0]], [0.257754, [3, -0.146667, 0], [3, 0.16, 0]], [1.4591, [3, -0.16, 0], [3, 0.16, 0]], [0.138102, [3, -0.16, 0], [3, 0.133333, 0]], [1.309, [3, -0.133333, 0], [3, 0.146667, 0]], [0.257754, [3, -0.146667, 0], [3, 0.266667, 0]], [0.372085, [3, -0.266667, 0], [3, 0.106667, 0]], [0.369652, [3, -0.106667, 0.00243296], [3, 0.28, -0.00638653]], [0.202446, [3, -0.28, 0], [3, 0.32, 0]], [0.369652, [3, -0.32, 0], [3, 0.28, 0]], [0.202446, [3, -0.28, 0], [3, 0.306667, 0]], [0.369652, [3, -0.306667, 0], [3, 0.28, 0]], [0.202446, [3, -0.28, 0], [3, 0.32, 0]], [0.369652, [3, -0.32, 0], [3, 0.28, 0]], [0.202446, [3, -0.28, 0], [3, 0.2, 0]], [0.82205, [3, -0.2, 0], [3, 0.2, 0]], [0.519567, [3, -0.2, 0.098122], [3, 0.0666667, -0.0327073]], [0.429562, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.72, 1.08, 1.52, 1.92, 2.36, 2.84, 3.32, 3.72, 4.16, 4.64, 5.08, 5.48, 5.92, 6.4, 6.88, 7.28, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 15.64, 16.24, 16.44])
    keys.append([[0.59515, [3, -0.253333, 0], [3, 0.12, 0]], [0.567232, [3, -0.12, 0.0279183], [3, 0.146667, -0.0341224]], [-0.851412, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.0750492, [3, -0.133333, -0.0667938], [3, 0.146667, 0.0734732]], [-0.00157596, [3, -0.146667, 0], [3, 0.16, 0]], [-0.460767, [3, -0.16, 0.141639], [3, 0.16, -0.141639]], [-0.851412, [3, -0.16, 0], [3, 0.133333, 0]], [-0.0750492, [3, -0.133333, -0.0667938], [3, 0.146667, 0.0734732]], [-0.00157596, [3, -0.146667, 0], [3, 0.16, 0]], [-0.460767, [3, -0.16, 0.147798], [3, 0.146667, -0.135481]], [-0.851412, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.0750492, [3, -0.133333, -0.0667938], [3, 0.146667, 0.0734732]], [-0.00157596, [3, -0.146667, 0], [3, 0.16, 0]], [-0.460767, [3, -0.16, 0.141639], [3, 0.16, -0.141639]], [-0.851412, [3, -0.16, 0], [3, 0.133333, 0]], [-0.0750492, [3, -0.133333, -0.0667938], [3, 0.146667, 0.0734732]], [-0.00157596, [3, -0.146667, -0.0505442], [3, 0.266667, 0.0918985]], [0.352279, [3, -0.266667, -0.0704895], [3, 0.106667, 0.0281958]], [0.380475, [3, -0.106667, -0.0244566], [3, 0.28, 0.0641986]], [0.618244, [3, -0.28, 0], [3, 0.32, 0]], [0.380475, [3, -0.32, 0], [3, 0.28, 0]], [0.618244, [3, -0.28, 0], [3, 0.306667, 0]], [0.380475, [3, -0.306667, 0], [3, 0.28, 0]], [0.618244, [3, -0.28, 0], [3, 0.32, 0]], [0.380475, [3, -0.32, 0], [3, 0.28, 0]], [0.618244, [3, -0.28, -0.172401], [3, 0.2, 0.123144]], [1.26711, [3, -0.2, 0], [3, 0.2, 0]], [1.23132, [3, -0.2, 0.0142061], [3, 0.0666667, -0.00473537]], [1.21028, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.72, 1.08, 1.52, 1.92, 2.36, 2.84, 3.32, 3.72, 4.16, 4.64, 5.08, 5.48, 5.92, 6.4, 6.88, 7.28, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24, 16.44])
    keys.append([[0.2, [3, -0.253333, 0], [3, 0.12, 0]], [0.95, [3, -0.12, 0], [3, 0.146667, 0]], [0.928, [3, -0.146667, 0.022], [3, 0.133333, -0.02]], [0.3, [3, -0.133333, 0.142794], [3, 0.146667, -0.157073]], [0.0283999, [3, -0.146667, 0], [3, 0.16, 0]], [0.75, [3, -0.16, -0.149933], [3, 0.16, 0.149933]], [0.928, [3, -0.16, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0.142794], [3, 0.146667, -0.157073]], [0.0283999, [3, -0.146667, 0], [3, 0.16, 0]], [0.75, [3, -0.16, -0.156452], [3, 0.146667, 0.143415]], [0.928, [3, -0.146667, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0.142794], [3, 0.146667, -0.157073]], [0.0283999, [3, -0.146667, 0], [3, 0.16, 0]], [0.75, [3, -0.16, -0.149933], [3, 0.16, 0.149933]], [0.928, [3, -0.16, 0], [3, 0.133333, 0]], [0.3, [3, -0.133333, 0], [3, 0.146667, 0]], [0.5284, [3, -0.146667, 0], [3, 0.266667, 0]], [0.271478, [3, -0.266667, 0.016695], [3, 0.106667, -0.00667799]], [0.2648, [3, -0.106667, 0.000304767], [3, 0.28, -0.000800014]], [0.264, [3, -0.28, 0], [3, 0.32, 0]], [0.2648, [3, -0.32, 0], [3, 0.28, 0]], [0.264, [3, -0.28, 0], [3, 0.306667, 0]], [0.2648, [3, -0.306667, 0], [3, 0.28, 0]], [0.264, [3, -0.28, 0], [3, 0.32, 0]], [0.2648, [3, -0.32, 0], [3, 0.28, 0]], [0.264, [3, -0.28, 0], [3, 0.4, 0]], [0.596785, [3, -0.4, 0], [3, 0.0666667, 0]], [0.2976, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.72, 1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24])
    keys.append([[0.915841, [3, -0.253333, 0], [3, 0.266667, 0]], [-1.19188, [3, -0.266667, 0], [3, 0.28, 0]], [0.995607, [3, -0.28, 0], [3, 0.32, 0]], [-1.19188, [3, -0.32, 0], [3, 0.28, 0]], [0.995607, [3, -0.28, 0], [3, 0.306667, 0]], [-1.19188, [3, -0.306667, 0], [3, 0.28, 0]], [0.995607, [3, -0.28, 0], [3, 0.32, 0]], [-1.19188, [3, -0.32, 0], [3, 0.28, 0]], [0.995607, [3, -0.28, -0.299664], [3, 0.266667, 0.285395]], [1.281, [3, -0.266667, -0.0368305], [3, 0.106667, 0.0147322]], [1.29573, [3, -0.106667, -0.0113707], [3, 0.28, 0.0298481]], [1.40466, [3, -0.28, 0], [3, 0.32, 0]], [1.29573, [3, -0.32, 0], [3, 0.28, 0]], [1.40466, [3, -0.28, 0], [3, 0.306667, 0]], [1.29573, [3, -0.306667, 0], [3, 0.28, 0]], [1.40466, [3, -0.28, 0], [3, 0.32, 0]], [1.29573, [3, -0.32, 0], [3, 0.28, 0]], [1.40466, [3, -0.28, -0.0242871], [3, 0.4, 0.0346958]], [1.47268, [3, -0.4, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.72, 1.08, 1.52, 1.92, 2.36, 2.84, 3.32, 3.72, 4.16, 4.64, 5.08, 5.48, 5.92, 6.4, 6.88, 7.28, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 15.64, 16.44])
    keys.append([[-0.905123, [3, -0.253333, 0], [3, 0.12, 0]], [-1.30837, [3, -0.12, 0], [3, 0.146667, 0]], [-0.966481, [3, -0.146667, 0], [3, 0.133333, 0]], [-1.23332, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.324005, [3, -0.146667, 0], [3, 0.16, 0]], [-1.23332, [3, -0.16, 0], [3, 0.16, 0]], [-0.966481, [3, -0.16, 0], [3, 0.133333, 0]], [-1.23332, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.324005, [3, -0.146667, 0], [3, 0.16, 0]], [-1.23332, [3, -0.16, 0], [3, 0.146667, 0]], [-0.966481, [3, -0.146667, 0], [3, 0.133333, 0]], [-1.23332, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.324005, [3, -0.146667, 0], [3, 0.16, 0]], [-1.23332, [3, -0.16, 0], [3, 0.16, 0]], [-0.966481, [3, -0.16, 0], [3, 0.133333, 0]], [-1.23332, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.324005, [3, -0.146667, 0], [3, 0.266667, 0]], [-0.397371, [3, -0.266667, 0.0112486], [3, 0.106667, -0.00449944]], [-0.401871, [3, -0.106667, 0], [3, 0.28, 0]], [-0.35585, [3, -0.28, 0], [3, 0.32, 0]], [-0.401871, [3, -0.32, 0], [3, 0.28, 0]], [-0.35585, [3, -0.28, 0], [3, 0.306667, 0]], [-0.401871, [3, -0.306667, 0], [3, 0.28, 0]], [-0.35585, [3, -0.28, 0], [3, 0.32, 0]], [-0.401871, [3, -0.32, 0], [3, 0.28, 0]], [-0.35585, [3, -0.28, -0.0177338], [3, 0.2, 0.012667]], [-0.310669, [3, -0.2, -0.0259024], [3, 0.266667, 0.0345366]], [-0.174533, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.72, 1.52, 2.36, 3.32, 4.16, 5.08, 5.92, 6.88, 7.72, 8.52, 8.84, 9.68, 10.64, 11.48, 12.4, 13.24, 14.2, 15.04, 16.24, 16.44])
    keys.append([[-0.401949, [3, -0.253333, 0], [3, 0.266667, 0]], [0.107338, [3, -0.266667, -0.130452], [3, 0.28, 0.136975]], [0.400331, [3, -0.28, 0], [3, 0.32, 0]], [0.107338, [3, -0.32, 0], [3, 0.28, 0]], [0.400331, [3, -0.28, 0], [3, 0.306667, 0]], [0.107338, [3, -0.306667, 0], [3, 0.28, 0]], [0.400331, [3, -0.28, 0], [3, 0.32, 0]], [0.107338, [3, -0.32, 0], [3, 0.28, 0]], [0.400331, [3, -0.28, 0], [3, 0.266667, 0]], [0.391888, [3, -0.266667, 0], [3, 0.106667, 0]], [0.395814, [3, -0.106667, -0.00261791], [3, 0.28, 0.00687202]], [0.420357, [3, -0.28, 0], [3, 0.32, 0]], [0.395814, [3, -0.32, 0], [3, 0.28, 0]], [0.420357, [3, -0.28, 0], [3, 0.306667, 0]], [0.395814, [3, -0.306667, 0], [3, 0.28, 0]], [0.420357, [3, -0.28, 0], [3, 0.32, 0]], [0.395814, [3, -0.32, 0], [3, 0.28, 0]], [0.420357, [3, -0.28, 0], [3, 0.4, 0]], [0.00501826, [3, -0.4, 0], [3, 0.0666667, 0]], [0.108872, [3, -0.0666667, 0], [3, 0, 0]]])

    try:
      # uncomment the following line and modify the IP if you use this script outside Choregraphe.
      # motion = ALProxy("ALMotion", IP, 9559)
      motion = srv["motion"]
      motion.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
      print err

