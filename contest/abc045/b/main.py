# 入力を受け取る
Sa = input()
Sb = input()
Sc = input()

# 初期ターンを 'A' とする
turn = 'A'

# 無限ループでカードが無くなるまでゲームを進行
while True:
    if turn == 'A':
        if len(Sa) == 0:  # Aさんのカードが無くなったらAさんの勝利
            print('A')
            break
        # Aさんのターン: 先頭のカードを捨てて次のターンへ
        turn = Sa[0].upper()  # 次のターンはSaの先頭の文字に基づく
        Sa = Sa[1:]  # カードを1枚捨てる
    elif turn == 'B':
        if len(Sb) == 0:  # Bさんのカードが無くなったらBさんの勝利
            print('B')
            break
        # Bさんのターン: 先頭のカードを捨てて次のターンへ
        turn = Sb[0].upper()  # 次のターンはSbの先頭の文字に基づく
        Sb = Sb[1:]  # カードを1枚捨てる
    elif turn == 'C':
        if len(Sc) == 0:  # Cさんのカードが無くなったらCさんの勝利
            print('C')
            break
        # Cさんのターン: 先頭のカードを捨てて次のターンへ
        turn = Sc[0].upper()  # 次のターンはScの先頭の文字に基づく
        Sc = Sc[1:]  # カードを1枚捨てる
