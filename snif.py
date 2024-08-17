#"crowd relax luggage gift runway believe bar hour desk virus glimpse unusual"
try:
    import mnemonic
    from eth_account import Account
    from bip32 import BIP32
    import binascii
    import requests
    import random
    import os
except:
    pass

# Очистим консоль перед выводом нового текста (для чистоты вывода)
os.system('cls' if os.name == 'nt' else 'clear')

# Текст или цифра, которые вы хотите отобразить вверху консоли
top_text = "Поиск запущен"

# Выводим текст вверху
print("=" * 50)
print(top_text.center(50))
print("=" * 50)
print()

i = 0

while True:
    i = i + 1
    def generate_mnemonic_from_file(file_path, num_words=12):
        # Чтение слов из файла
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]

        # Генерация сид-фразы
        mnemonic = ' '.join(random.sample(words, num_words))
        return mnemonic


    # Укажите путь к вашему файлу
    file_path = 'english.txt'
    num_words = 12  # Количество слов в сид-фразе (например, 12 для BIP-39)

    seed_phrase = generate_mnemonic_from_file(file_path, num_words)
    # Получаем seed из сид-фразы
    seed = mnemonic.Mnemonic.to_seed(seed_phrase)

    # Создаем объект BIP32
    bip32 = BIP32.from_seed(seed)

    # Путь BIP-44 для Ethereum (m/44'/60'/0'/0/0)
    bip32_path = "m/44'/60'/0'/0/0"
    key = bip32.get_privkey_from_path(bip32_path)

    # Приватный ключ в формате Ethereum
    private_key = binascii.hexlify(key).decode()

    # Создаем Ethereum-адрес из приватного ключа
    account = Account.from_key(private_key)
    address = account.address

    # Замените YOUR_ETHERSCAN_API_KEY на ваш API ключ
    etherscan_api_key = "SD8YJFBVPJJTQMUMBC7E4THCNJZ9MPQS6H"

    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={etherscan_api_key}"
    response = requests.get(url)
    data = response.json()
    balance = int(data['result'])
    print(f" {i} | {balance} ETH | {address}")
    if balance > 0:
        print(f"\n\n {i} | {balance} ETH | {address} | {seed_phrase}")
        with open('eth_address.txt', 'w') as f:
            f.write(f" {i} | {balance} ETH | {address} | {seed_phrase}")
            f.close()
        break




