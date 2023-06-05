from function import multi_set_fusion

Theta = {'A', 'B', 'C'}
RPS1 = {'A': 0.12, 'B': 0.10, 'AB': 0.15, 'BA': 0.15, 'AC': 0.03, 'ABC': 0.10, 'ACB': 0.25, 'BAC': 0.08, 'CAB': 0.02}
RPS2 = {'A': 0.10, 'B': 0.15, 'AB': 0.07, 'BA': 0.23, 'AC': 0.10, 'ABC': 0.10, 'ACB': 0.05, 'BAC': 0.12, 'CAB': 0.08}
RPS3 = {'A': 0.18, 'B': 0.05, 'AB': 0.15, 'BA': 0.05, 'AC': 0.00, 'ABC': 0.12, 'ACB': 0.30, 'BAC': 0.10, 'CAB': 0.05}
list_RPS = [RPS3, RPS1, RPS2]
result = multi_set_fusion(Theta, 'left', list_RPS)
for item in result:
    print(item)
