import random
import timeit
import requests
import io

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено


def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):

    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

        return -1
    

def polynomial_hash(s, base=256, modulus=101):

    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)
    
    base = 256 
    modulus = 101  
    
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

def timer(string, func, text,pattern):
    start = timeit.default_timer()
    print(string)
    func(text,pattern)

    print("Time consumed :", timeit.default_timer() - start)
    print("\n")

def downloading_files(url, name):
    response = requests.get(url)
    if response.status_code == 200:
        with open(name, 'w', encoding='utf-8') as file:
            file.write(response.text)
            file.close()
        with io.open(name, 'r', encoding='utf-8', errors='ignore') as file:
            file1 = file.read()
        return file1
    else:
        print(f"Failed to retrieve the file. Status code: {response.status_code}")

def main():
    target_url1="https://drive.google.com/uc?export=download&id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"
    target_url2="https://drive.google.com/uc?export=download&id=18BfXyQcmuinEI_8KDSnQm4bLx6yIFS_w"
    name1="text_1.txt"
    name2="text_2.txt"

    file1=downloading_files(target_url1,name1)
    file2= downloading_files(target_url2,name2)
    
    pattern_exist="Жадібний алгоритм у цьому"
    pattern_no="aosjkjbhjsabkscbsaax"

    timer("Алгоритм Боєра-Мура",boyer_moore_search,file1, pattern_exist)
    timer("Алгоритм Кнута-Морріса-Пратта",kmp_search,file1,pattern_exist)
    timer("Алгоритм Рабіна-Карпа", rabin_karp_search,file1,pattern_exist)

    print("______________________________________________")

    timer("Алгоритм Боєра-Мура",boyer_moore_search,file2, pattern_no)
    timer("Алгоритм Кнута-Морріса-Пратта",kmp_search,file2,pattern_no)
    timer("Алгоритм Рабіна-Карпа", rabin_karp_search,file2,pattern_no)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
