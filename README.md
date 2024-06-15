GitHubdan o'zgarishlarni olish va botingizni qayta ishga tushirish uchun quyidagi qadamlarni bajaring:

### 1. O'zgarishlarni GitHubdan olish (pull)

1. **Virtual muhitga kirish** (agar hali faollashtirilmagan bo'lsa):
   ```sh
   source ~/taxi-bot/venv/bin/activate
   ```

2. **Loyihangiz katalogiga o'ting**:
   ```sh
   cd ~/taxi-bot
   ```

3. **GitHubdan o'zgarishlarni olish**:
   ```sh
   git pull origin main
   ```
   (Bu yerda `main` sizning asosiy branch nomingiz, agar boshqa branch ishlatilgan bo'lsa, o'sha branch nomini yozing)

### 2. Python kutubxonalarini yangilash (agar requirements.txt o'zgargan bo'lsa)

Agar `requirements.txt` faylida o'zgarishlar bo'lsa, yangi kutubxonalarni o'rnating:
   ```sh
   pip install -r requirements.txt
   ```

### 3. Xizmat sifatida qayta ishga tushirish

Agar botingiz xizmat sifatida sozlangan bo'lsa, xizmatni qayta ishga tushiring:

1. **Xizmatni qayta yuklash** (daemon reload) va qayta ishga tushirish:
   ```sh
   sudo systemctl daemon-reload
   sudo systemctl restart taxi-bot
   ```

### 4. Qo'lda qayta ishga tushirish

Agar botingizni qo'lda ishlatgan bo'lsangiz, botni to'xtating va qayta ishga tushiring:

1. **Avvalgi bot jarayonini to'xtating**:
   ```sh
   ps aux | grep python
   ```
   - Jarayonni topib, uni to'xtating:
     ```sh
     kill -9 <PID>
     ```

2. **Virtual muhitga kirish**:
   ```sh
   source ~/taxi-bot/venv/bin/activate
   ```

3. **Botni ishga tushirish**:
   ```sh
   python ~/taxi-bot/app.py
   ```

### 5. `nohup` yoki `screen` yordamida fon rejimida ishga tushirish

Agar botni fon rejimida ishlatishni istasangiz:

#### `nohup` yordamida:
```sh
nohup python ~/taxi-bot/app.py &
```

#### `screen` yordamida:
1. Yangi `screen` sessiyasini boshlash:
   ```sh
   screen -S taxi-bot
   ```

2. Virtual muhitga kirish:
   ```sh
   source ~/taxi-bot/venv/bin/activate
   ```

3. Botni ishga tushirish:
   ```sh
   python ~/taxi-bot/app.py
   ```

4. `screen` sessiyasidan chiqish:
   ```sh
   Ctrl + A, D
   ```

Bu qadamlar botingizni GitHubdan o'zgarishlarni olib qayta ishga tushirishga yordam beradi. Agar qo'shimcha yordam yoki savollar bo'lsa, bemalol so'rang!