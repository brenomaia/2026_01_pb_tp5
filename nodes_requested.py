VMS_REQUESTED = [
    48, 12, 35, 22, 17, 65, 8, 42, 53, 29,
    14, 38, 47, 19, 25, 61, 33, 9, 55, 23,
    44, 16, 50, 31, 11, 28, 58, 41, 13, 37,
    62, 21, 45, 18, 26, 52, 34, 7, 49, 20,
    39, 15, 57, 32, 12, 27, 54, 43, 10, 36,
    60, 24, 46, 16, 22, 51, 30, 8, 40, 25
]

SERVER_CAPACITY = 100

def next_fit(vms_request: list[int], capacity: int) -> list[list[int]]:
    open_servers = [[]]

    for vm_request in vms_request:
        current_capacity = sum(open_servers[-1])
        if current_capacity + vm_request <= capacity:
            open_servers[-1].append(vm_request)
        else:
            open_servers.append([vm_request])

    return open_servers


def first_fit_decreasing(vms_request: list[int], capacity: int) -> list[list[int]]:
    open_servers = [[]]
    vms_request_reverse_order = merge_sort_desc(vms_request)

    for vm_request in vms_request_reverse_order:
        for idx in range(len(open_servers)):
            current_capacity = sum(open_servers[idx])
            if current_capacity + vm_request <= capacity:
                open_servers[idx].append(vm_request)
                break
            elif idx == len(open_servers)-1:
                open_servers.append([vm_request])

    return open_servers


def merge_sort_desc(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    
    array_1 = merge_sort_desc(array[0:(len(array) // 2)])
    array_2 = merge_sort_desc(array[(len(array) // 2):])

    array_1_idx = 0
    array_2_idx = 0

    result_array = []

    while (array_1_idx < len(array_1)) or (array_2_idx < len(array_2)):
        if (array_1_idx < len(array_1)) and (array_2_idx < len(array_2)):
            if array_1[array_1_idx] > array_2[array_2_idx]:
                result_array.append(array_1[array_1_idx])
                array_1_idx += 1
            else:
                result_array.append(array_2[array_2_idx])
                array_2_idx += 1
            continue

        if (array_1_idx < len(array_1)):
            result_array.append(array_1[array_1_idx])
            array_1_idx += 1

        if (array_2_idx < len(array_2)):
            result_array.append(array_2[array_2_idx])
            array_2_idx += 1

    return result_array

    
    

next_fit_result = next_fit(VMS_REQUESTED, SERVER_CAPACITY)
first_fit_decreasing_result = first_fit_decreasing(VMS_REQUESTED, SERVER_CAPACITY)

print(f"""
=== RESULTADO DA ALOCAÇÃO (HEURÍSTICAS) ===
[Heurística Next-Fit]
- Servidores utilizados: {len(next_fit_result)} servidores
- Exemplo de ocupação do Servidor 1: {next_fit_result[0]} (Total: {sum(next_fit_result[0])}/100 GB)

[Heurística First-Fit Decreasing]
- Servidores utilizados: {len(first_fit_decreasing_result)} servidores
- Exemplo de ocupação do Servidor 1: {first_fit_decreasing_result[0]} (Total: {sum(first_fit_decreasing_result[0])}/100 GB)
Conclusão: A heurística First-Fit Decreasing economizou {abs(len(next_fit_result)) - len(first_fit_decreasing_result)}
servidores em relação à Next-Fit.
      """)