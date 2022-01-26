from collections import Counter
import heapq


def huffman_encode(text):
    letters_heap = [(count, char) for char, count in Counter(text).items()]
    heapq.heapify(letters_heap)
    node_list = create_node_tree(letters_heap)
    letters_code = create_letters_coding(node_list)
    encoded_text = ''
    for char in text:
        encoded_text += letters_code[char]
    return encoded_text, letters_code


def create_node_tree(letters_heap: heapq):
    tree = []
    while len(letters_heap) > 1:
        count1, right = heapq.heappop(letters_heap)
        count2, left = heapq.heappop(letters_heap)
        heapq.heappush(letters_heap, (count1 + count2, left + right))
        tree.append((right, '1'))
        tree.append((left, '0'))
    return tree


def create_letters_coding(tree):
    letters_coding = {}
    for el, b in tree[::-1]:
        for char in el:
            code = letters_coding.get(char, '')
            letters_coding[char] = code + b
    return letters_coding


def huffman_decode(encoded_text, letters_code):
    decoded_text = ''
    while encoded_text:
        for char, code in letters_code.items():
            if encoded_text.startswith(code):
                decoded_text += char
                encoded_text = encoded_text[len(code):]
    return decoded_text


if __name__ == '__main__':
    text = "Eхал грека через реку, видит грека в реке рак. сунул грека руку в реку, рак за руку греку цап."
    encoded_text, letters_code = huffman_encode(text)
    print(encoded_text)
    decoded_text = huffman_decode(encoded_text, letters_code)
    print(decoded_text)
    print(decoded_text == text)
