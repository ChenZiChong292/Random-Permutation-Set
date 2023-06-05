from orderedset import OrderedSet
# Due to the consideration of the order of sets in a random permutation set, it is necessary to use ordered sets.


class RandomPermutationSet:
    def __init__(self, PES, RPS1, RPS2):
        # PES is the permutation event space
        # RPS is the random permutation set
        self.PES = PES
        self.RPS1 = RPS1
        self.RPS2 = RPS2

    # A_right_intersection_B is to calculate the right intersection (RI)
    def A_right_intersection_B(self, setA, setB):
        string = ''
        string_setB = ''
        setA = OrderedSet(setA)
        setB = OrderedSet(setB)
        center_set = (self.PES.intersection(setB)).intersection((self.PES - setA))
        string = string.join(center_set)
        string_setB = string_setB.join(setB)
        out = string_setB
        for ch in string:
            out = out.replace(ch, '')
        return OrderedSet(out)

    # A_left_intersection_B is to calculate the left intersection (LI)
    def A_left_intersection_B(self, setA, setB):
        string = ''
        string_setA = ''
        setA = OrderedSet(setA)
        setB = OrderedSet(setB)
        center_set = (self.PES.intersection(setA)).intersection((self.PES - setB))
        string = string.join(center_set)
        string_setA = string_setA.join(setA)
        out = string_setA
        for ch in string:
            out = out.replace(ch, '')
        return OrderedSet(out)

    # right_conflict_coefficient is to calculate right conflict coefficient
    def right_conflict_coefficient(self):
        K = 0
        for B, VB in self.RPS1.items():
            for C, VC in self.RPS2.items():
                if len(self.A_right_intersection_B(B, C)) == 0:
                    K = K + VB * VC
        return K

    # left_conflict_coefficient is to calculate left conflict coefficient
    def left_conflict_coefficient(self):
        K = 0
        for B, VB in self.RPS1.items():
            for C, VC in self.RPS2.items():
                if len(self.A_left_intersection_B(B, C)) == 0:
                    K = K + VB * VC
        return K

    # right_orthogonal_sum is the left orthogonal sum (ROS)
    def right_orthogonal_sum(self, K):
        coe = 1 / (1 - K)
        res = {}
        for B, VB in self.RPS1.items():
            for C, VC in self.RPS2.items():
                temp = self.A_right_intersection_B(B, C)
                if len(temp) == 0:
                    continue
                else:
                    Set = ''.join(list(temp))
                    if Set in res.keys():
                        res[Set] = res[Set] + VB * VC
                    else:
                        res.setdefault(Set, VB * VC)
        for Key, Val in res.items():
            res[Key] = round(Val * coe, 3)
        return res

    # left_orthogonal_sum is the left orthogonal sum (LOS)
    def left_orthogonal_sum(self, K):
        coe = 1 / (1 - K)
        res = {}
        for B, VB in self.RPS1.items():
            for C, VC in self.RPS2.items():
                temp = self.A_left_intersection_B(B, C)
                if len(temp) == 0:
                    continue
                else:
                    Set = ''.join(list(temp))
                    if Set in res.keys():
                        res[Set] = res[Set] + VB * VC
                    else:
                        res.setdefault(Set, VB * VC)
        for Key, Val in res.items():
            res[Key] = round(Val * coe, 3)
        return res
