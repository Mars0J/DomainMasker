# MARS BABA BIR NUMARA 


addon = """
                            
                                    ╱╱╱╱╱╭╮╱╱╭╮╭╮╱╱╱╱╱╱╱╱╱╱╱╭━╮
                                    ╭━┳━┳╯┣━┳╯┃┃╰┳┳╮╭━━┳━╮╭┳┫━┫
🇩​​​​​🇴​​​​​🇲​​​​​🇦​​​​​🇮​​​​​̇🇳​​​​​ 🇲​​​​​🇦​​​​​🇸​​​​​🇰​​​​​🇪​​​​​🇷​​​​    ▄▄                  ┃━┫╋┃╋┃┻┫╋┃┃╋┃┃┃┃┃┃┃╋╰┫╭╋━┃
                                    ╰━┻━┻━┻━┻━╯╰━╋╮┃╰┻┻┻━━┻╯╰━╯
                                    ╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯

"""









import sys , argparse
from urllib.parse import urlparse
from requests import post


def kısaltma(big_url: str) -> str:
    return post(f"https://is.gd/create.php?format=json&url={big_url}").json()['shorturl']


def maskeleme(target_url: str, mask_domain: str, keyword: str) -> str:
    url = kısaltma(target_url)
    return f"{mask_domain}-{keyword}@{urlparse(url).netloc + urlparse(url).path}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="URLyi Başka Bir URL nin Üstüne Maskeleniyor")

    parser.add_argument(
        "--hedef",
        type=str,
        help="Maskelenecek Hedef URL (http veya https)",
        required=True,
    )
    parser.add_argument(
        "--maske",
        type=str,
        help="Maskelemek istediginiz URL (http veya https)",
        required=True,
    )

    parser.add_argument(
        "--anahtar",
        type=str,
        help="anahtar kelimeler (Bosluk icin (-) ile gecin)",
        required=True,
    )

    print(f"\033[91m {addon}\033[00m]")

    if len(sys.argv) == 1:
        print("\n")
        hedef= input("URLyi Girin (http veya https) : ")
        maske= input("maskelemek için bir alan adı girin (http veya https) : ")
        anahtar= input("anahtarı girin (boş geçmek için (-) ) : ")
    else:
        args = parser.parse_args()
        hedef = args.hedef
        maske = args.maske
        anahtar = args.anahtar

    
    print(f"\033[91m {maskeleme(hedef, maske, anahtar)}\033[00m")
