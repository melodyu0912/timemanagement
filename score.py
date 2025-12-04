from collections import OrderedDict

# 讀取使用者名稱與聲譽分數，直到輸入 'q'
users_order = []
reputation = OrderedDict()
keyword_counts = {}

keywords = ['戶頭','銀行','下單','帳號','匯','欠款','檢察官','警察','提款機','點數','發票','援交','酒店','股票','投資','顧問','課程','專員','平台']

while True:
    line = input().strip()
    if line == 'q':
        break
    if not line:
        continue
    parts = line.split()
    if len(parts) < 2:
        continue
    name = parts[0]
    try:
        score = int(parts[1])
    except ValueError:
        # 忽略格式錯誤的行
        continue
    users_order.append(name)
    reputation[name] = score
    keyword_counts[name] = 0

# 第二階段：讀取用戶名稱與訊息直到輸入 'q'
flagged = {name: (reputation[name] <= 3) for name in users_order}

while True:
    try:
        line = input()
    except EOFError:
        break
    if line is None:
        break
    line = line.rstrip('\n')
    if line == 'q':
        break
    if not line:
        continue
    parts = line.split(' ', 1)
    name = parts[0]
    msg = parts[1] if len(parts) > 1 else ''
    if name not in reputation:
        # 忽略不在使用者名單內的訊息
        continue

    # 計算關鍵字出現次數（每個關鍵字在訊息中可出現多次）
    cnt = 0
    for kw in keywords:
        if kw in msg:
            # 使用 str.count 以計算同一訊息中多次出現
            k = msg.count(kw)
            cnt += k
    if cnt:
        keyword_counts[name] += cnt

    # 若聲譽分數 <= 3 或 關鍵字總次數超過 2 即為潛在詐騙
    if reputation[name] <= 3 or keyword_counts[name] > 2:
        flagged[name] = True
        print('小心詐騙!')

# 輸出所有被列為潛在詐騙的用戶名稱，依照最初輸入順序
for name in users_order:
    if flagged.get(name):
        print(name)