def hanoi_towers(num: int, start_col: int, end_col: int) -> None:
    if num == 1:
        print(f"Перемещаем блинчик {num = } из {start_col = } в {end_col = }")
        return
    intermed = 6 - start_col - end_col
    hanoi_towers(num - 1, start_col, intermed)
    print(f"Перемещаем блинчик {num = } из {start_col = } в {end_col = }")
    hanoi_towers(num - 1, intermed, end_col)

hanoi_towers(5, 1, 3)