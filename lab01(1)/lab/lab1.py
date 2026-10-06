from tkinter import Tk, filedialog, Label, Button, Text, Entry, Frame
from math import log2
from collections import Counter
import heapq
import sys
from bisect import bisect_left


#Алгоритмы 
sys.setrecursionlimit(10000)

def shannon_fano(text):
    if not text:
        return {}

    freq = Counter(text)
    total = len(text)

    probs = {ch: cnt / total for ch, cnt in freq.items()}
    chars = sorted(probs.keys(), key=lambda ch: -probs[ch])
    n = len(chars)

    prefix_sums = [0.0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + probs[chars[i]]

    codes = {}
    stack = [(0, n, "")]

    while stack:
        start, end, prefix = stack.pop()

        if end - start == 1:
            codes[chars[start]] = prefix or "0"
            continue

        target = (prefix_sums[start] + prefix_sums[end]) / 2.0
        split_idx = bisect_left(prefix_sums, target, start + 1, end)

        best_i = split_idx
        if best_i >= end:
            best_i = end - 1

        if best_i > start + 1:
            diff1 = abs(2 * prefix_sums[best_i] - prefix_sums[start] - prefix_sums[end])
            diff2 = abs(2 * prefix_sums[best_i - 1] - prefix_sums[start] - prefix_sums[end])
            if diff2 < diff1:
                best_i -= 1

        stack.append((best_i, end, prefix + "1"))
        stack.append((start, best_i, prefix + "0"))

    return codes


def huffman(text):
    freq = Counter(text)
    total = len(text)
    probs = {ch: cnt / total for ch, cnt in freq.items()}

    heap = [[p, i, ch] for i, (ch, p) in enumerate(probs.items())]
    heapq.heapify(heap)
    n = len(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        heapq.heappush(heap, [lo[0] + hi[0], n, [lo, hi]])
        n += 1

    codes = {}
    def walk(node, code):
        if isinstance(node[2], str):
            codes[node[2]] = code or "0"
        else:
            walk(node[2][0], code + "0")
            walk(node[2][1], code + "1")

    walk(heap[0], "")
    return codes


def stats(text, codes):
    total = len(text)
    probs = {ch: cnt / total for ch, cnt in Counter(text).items()}
    H = -sum(p * log2(p) for p in probs.values() if p > 0)
    L = sum(probs[ch] * len(codes[ch]) for ch in probs)
    R = (L - H) / L if L > 0 else 0
    return H, L, R


#Интерфейс 

current_text = ""      
total_len = 0          


def load_file():
    global current_text, total_len

    filepath = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=[("Текстовые файлы", "*.txt")]
    )
    if not filepath:
        return

    with open(filepath, "r", encoding="utf-8") as f:
        current_text = f.read()
    total_len = len(current_text)

    codes_sf = shannon_fano(current_text)
    H_sf, L_sf, R_sf = stats(current_text, codes_sf)
    show_result(text_sf, H_sf_entry, L_sf_entry, R_sf_entry,
                codes_sf, H_sf, L_sf, R_sf)

    codes_hf = huffman(current_text)
    H_hf, L_hf, R_hf = stats(current_text, codes_hf)
    show_result(text_hf, H_hf_entry, L_hf_entry, R_hf_entry,
                codes_hf, H_hf, L_hf, R_hf)

def show_result(text_widget, h_entry, l_entry, r_entry, codes, H, L, R):
    probs = {ch: cnt / total_len for ch, cnt in Counter(current_text).items()}
    text_widget.delete("1.0", "end")
    # заголовок таблицы
    text_widget.insert("end", f"{'символ':<8}{'P':<10}{'код':<15}\n")
    text_widget.insert("end", "-" * 35 + "\n")
    # строки, отсортированные по убыванию вероятности
    for ch in sorted(probs, key=lambda c: -probs[c]):
        display = {"\n": "\\n", " ": "␣", "\t": "\\t"}.get(ch, ch)
        text_widget.insert(
            "end",
            f"'{display}'{'':<5}{probs[ch]:<10.4f}{codes[ch]:<15}\n"
        )
    h_entry.delete(0, "end"); h_entry.insert(0, f"{H:.4f}")
    l_entry.delete(0, "end"); l_entry.insert(0, f"{L:.4f}")
    r_entry.delete(0, "end"); r_entry.insert(0, f"{R:.4f}")

root = Tk()
root.title("Кодирование")
root.geometry("720x600")

# Кнопка загрузки
Button(root, text="Загрузить сообщение", command=load_file).grid(
    row=0, column=0, columnspan=2, sticky="we", padx=10, pady=10
)

# Заголовки колонок
Label(root, text="Кодирование Шеннона-Фано").grid(row=1, column=0, pady=(0, 5))
Label(root, text="Кодирование Хаффмана").grid(row=1, column=1, pady=(0, 5))

# Текстовые поля с кодами
text_sf = Text(root, width=40, height=20, bg="lightgray")
text_sf.grid(row=2, column=0, padx=10, sticky="nsew")

text_hf = Text(root, width=40, height=20, bg="lightgray")
text_hf.grid(row=2, column=1, padx=10, sticky="nsew")

# Левая колонка метрик 
Label(root, text="Энтропия H(Z)").grid(row=3, column=0, sticky="w", padx=10, pady=(10, 0))
H_sf_entry = Entry(root, width=20)
H_sf_entry.grid(row=3, column=0, sticky="e", padx=10, pady=(10, 0))

Label(root, text="Среднее число символов\nна один знак сообщения").grid(
    row=4, column=0, sticky="w", padx=10
)
L_sf_entry = Entry(root, width=20)
L_sf_entry.grid(row=4, column=0, sticky="e", padx=10)

Label(root, text="Избыточность кода").grid(row=5, column=0, sticky="w", padx=10)
R_sf_entry = Entry(root, width=20)
R_sf_entry.grid(row=5, column=0, sticky="e", padx=10)

#  Правая колонка метрик 
Label(root, text="Энтропия H(Z)").grid(row=3, column=1, sticky="w", padx=10, pady=(10, 0))
H_hf_entry = Entry(root, width=20)
H_hf_entry.grid(row=3, column=1, sticky="e", padx=10, pady=(10, 0))

Label(root, text="Среднее число символов\nна один знак сообщения").grid(
    row=4, column=1, sticky="w", padx=10
)
L_hf_entry = Entry(root, width=20)
L_hf_entry.grid(row=4, column=1, sticky="e", padx=10)

Label(root, text="Избыточность кода").grid(row=5, column=1, sticky="w", padx=10)
R_hf_entry = Entry(root, width=20)
R_hf_entry.grid(row=5, column=1, sticky="e", padx=10)

# Растягивание колонок
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

root.mainloop()