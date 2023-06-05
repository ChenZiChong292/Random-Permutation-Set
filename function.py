from rps import RandomPermutationSet


# multi_set_fusion is the fusion rule of random permutation set, which achieves the fusion of multiple RPSs
# This function returns an RPS list that represents the results of each fusion.
# PES is the permutation event space
# inter is the form of intersection, 'left' represents left intersection, otherwise it represents right intersection
# list_RPS is a list that includes all RPS that need to be fused. The order in the list determines the fusion order

def multi_set_fusion(PES, inter, list_RPS):
    start_RPS = list_RPS[0]
    next_RPS = list_RPS[1]
    fusion_result = []
    index = 1
    for i in range(1, len(list_RPS)):
        if inter == 'left':
            RPS = RandomPermutationSet(PES, start_RPS, next_RPS)
            K = RPS.left_conflict_coefficient()
            temp_RPS = RPS.left_orthogonal_sum(K)
        else:
            RPS = RandomPermutationSet(PES, start_RPS, next_RPS)
            K = RPS.right_conflict_coefficient()
            temp_RPS = RPS.right_orthogonal_sum(K)
        fusion_result.append(temp_RPS)
        index = index + 1
        if index < len(list_RPS):
            next_RPS = list_RPS[index]
            start_RPS = temp_RPS
    return fusion_result
