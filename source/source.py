import os 
import random
sites = [
"https://www.youtube.com/watch?v=fF4DXK1dpzA",
"https://www.youtube.com/watch?v=_iFYePfdDmw",
"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.wondershare.com%2Frecoverit%2Farticle%2F11%2Flinux-vs-windows-8.jpg&f=1&nofb=1&ipt=e6bb6fda593ade9172897ab38d56a11f3c74da209b295b9c07361c2237e9d69c",
"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fotlichaet.com%2Fwp-content%2Fuploads%2F1%2F6%2Fb%2F16b75dc30f7686fe72929da6f3e258b2.jpeg&f=1&nofb=1&ipt=6fcc2989a6a5df7461e4b7bfe8ddc3ecf3cf348f5bd15ab1425fe937df2432ad",
"https://www.youtube.com/watch?v=2NZSxvyaBMo",
"https://lifehacker.ru/linux-luchshe-windows/",
"https://lifehacker.ru/linux-vs-windows/",
"https://habr.com/ru/articles/716394/",
"https://ru.wikihow.com/%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D1%8C-Linux",
"https://lifehacker.ru/kak-ustanovit-linux/",
"https://preview.redd.it/linux-vs-windows-v0-tjzumypv3i9f1.jpeg?width=640&crop=smart&auto=webp&s=311d2b098b9b927ec46ef6630456e2703af7ac3f",
"https://wiki.gentoo.org/wiki/Handbook:Main_Page/ru",
"https://wiki.archlinux.org/title/Installation_guide_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)",
"https://i.redd.it/3fmbi9gjqw8f1.jpeg",
"https://preview.redd.it/based-on-a-recent-event-v0-2duj85sd1p2f1.png?width=640&crop=smart&auto=webp&s=f5ed6a66ad88e07e5988dc929871e9ce258b0e23",
"https://www.youtube.com/watch?v=W09yByavkn0",
"https://www.youtube.com/watch?v=8h4Bx0b8Xto",
"https://www.youtube.com/watch?v=u3Rsr8OVaZY&t=2s&pp=0gcJCcEJAYcqIYzv",
"https://www.youtube.com/watch?v=1y8dcYvwUhc"
]  
os.system("start " + random.SystemRandom().choice(sites))
