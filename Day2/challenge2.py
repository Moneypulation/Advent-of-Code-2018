# To remove the newlines, I just used a find-and-replace feature from an editor
def differPosition(s1, s2):
    if len(s1) != len(s2):
        return -1
    pos = -1

    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            if pos != -1:
                return -1
            else:
                pos = i

    return pos

str = "luojygedpvsthptkxiwnaorzmq, lucjqgedppsbhftkxiwnaorlmq, lucjmgefpvsbhftkxiwnaorziq, lucjvgedpvsbxftkxiwpaorzmq, lrcjygedjvmbhftkxiwnaorzmq, lucjygedpvsbhftkxiwnootzmu, eucjygedpvsbhftbxiwnaorzfq, lulnygedpvsbhftkxrwnaorzmq, lucsygedpvsohftkxqwnaorzmq, lucjyaedpvsnhftkxiwnaorzyq, lunjygedpvsohftkxiwnaorzmb, lucjxgedpvsbhrtkxiwnamrzmq, lucjygevpvsbhftkxcwnaorzma, lucjbgedpvsbhftrxiwnaoazmq, llcjygkdpvhbhftkxiwnaorzmq, lmcjygxdpvsbhftkxswnaorzmq, lucpygedpvsbhftkxiwraorzmc, lucjbgrdpvsblftkxiwnaorzmq, lucjfgedpvsbhftkxiwnaurzmv, lucjygenpvsbhytkxiwnaorgmq, luqjyredsvsbhftkxiwnaorzmq, lucjygedpvavhftkxiwnaorumq, gucjygedpvsbhkxkxiwnaorzmq, lucjygedpvsbhftkxlwnaordcq, lucjygedpvibhfqkxiwnaorzmm, lucjegedpvsbaftkxewnaorzmq, kucjygeqpvsbhfokxiwnaorzmq, lugjygedwvsbhftkxiwnatrzmq, lucjygedqvsbhftdxiwnayrzmq, lucjygekpvsbuftkxiwnaqrzmq, lucjygedpvsbhfbkxiwnaoozdq, lscjygedpvzchftkxiwnaorzmq, luckygedpvsbxftkxiwnaorvmq, luyjygedgvsbhptkxiwnaorzmq, lmcjygedpvsbhfckxiwnaodzmq, lucmygedwvybhftkxiwnaorzmq, lgcjhgedavsbhftkxiwnaorzmq, lucjugedpvsbhftkxiwmaoozmq, lucjygedpvybhftkxkwnaorumq, lucjygedpvzbhfakxiwnaorzpq, lucjygedpvsbhftyxzwnajrzmq, lucjygedpvsdhfakxiwnoorzmq, luyjygeopvhbhftkxiwnaorzmq, lucjygadpvsbhntkxiwnaorzmx, lucjygedzvsbhftkiiwuaorzmq, sucjygodpvsbhftkxiwuaorzmq, euijygydpvsbhftkxiwnaorzmq, lucjlgeduvsbhftkxicnaorzmq, lucjdgedpvsbhfgkxiwnhorzmq, lucjymedpvsbhotkxiqnaorzmq, lucjygmdpvsbhftkxywnairzmq, lucjggedpvsbhfxkxiqnaorzmq, sucjygedpvsbhftkxiwnaorjmv, lucjlgedpvsbhftkxiwnairzmg, lucjygedppubhftkxijnaorzmq, lucjyxedpvsvhftkxlwnaorzmq, lucjygedpvxbhftkfiwyaorzmq, lucjygedposbhftkniwnaorzmw, lucjygewpvsbhftgxiwnavrzmq, lucjynedpvsbmftkaiwnaorzmq, lucjyhedpvzbhftkxiwncorzmq, lucjygedpvsbhfikpiwnaoezmq, lupjypedpvsbhftkjiwnaorzmq, lucjygudpvsbhfwkxivnaorzmq, lucjygrdpvsbhatkxzwnaorzmq, lucjbgmdpvsbhftkxihnaorzmq, lucjmgedpvpbhftkxiwnaorcmq, lucjygedpvskhfukmiwnaorzmq, lucjygedgvsbhftkxiwnvprzmq, lucjzgedppsbhytkxiwnaorzmq, lfcjypedpvsbhftrxiwnaorzmq, lucjyqldphsbhftkxiwnaorzmq, lucjygedpvsbhftzxewnaorzqq, lucjygeapvsbhftkxiinoorzmq, lucjygedpvszhftguiwnaorzmq, luojygedpvsbhftkxawnaornmq, lucjygedpcsboetkxiwnaorzmq, lufjygedpvfbhftaxiwnaorzmq, luciygedpvsbhftkxhwaaorzmq, lucjygedpvnbhftkaiwnaorzmc, lucjygedpvsbhftkxiwcaorbdq, lucjygelpvsbhftaxiwsaorzmq, lujjygedpssbhftkxiwnaorzmr, ludjygedpvsbhftkxiynaorzmj, lukjygeedvsbhftkxiwnaorzmq, lucjqpedpvsbhftkxiwnaozzmq, jucjygedpvsbhftkxgwnaorqmq, llwjygedpvsbhetkxiwnaorzmq, rucjygedpvsbhftkxiwndorymq, lucjygedpvsbhftvxswnaorwmq, lucjygerpvsbhfykxiwnaormmq, lucjynedpvsbhftkxijnaorziq, ljcjygedpvrbhftkeiwnaorzmq, lucjygedpnsbhftkxiwhaornmq, lucjygadpvsbhftkxibnaorzqq, lucjqgedpvsihftkxiwnaorzdq, lucjygedpvsqhfttjiwnaorzmq, llcjygedsvsbhftkxiwwaorzmq, lfckygedpvsbhftkxiunaorzmq, lucjyeedpdsbhftkxiwnaotzmq, lucjygedpvsbhftkoiwnaoqzcq, huwjvgedpvsbhftkxiwnaorzmq, lucjygldpvsbdhtkxiwnaorzmq, lycxygedpvsbhftmxiwnaorzmq, lucjygedpvsbhftyxianvorzmq, lucuygedpdsbhqtkxiwnaorzmq, lucjyggdpvsbhftkxiwnavremq, lucjyggdpvsbkftkxiwnaorbmq, luchyqedpvsbhftixiwnaorzmq, lpcnygedpvsbhftkxzwnaorzmq, lucjygedpvsihftkxiwfaortmq, lucjygvdpvsbhgtkxiwnamrzmq, lucjygodpvrbhqtkxiwnaorzmq, lucjygedpfsbhftkxipnaorzma, lucjygedpvsbhftkxpcjaorzmq, lucjygodbmsbhftkxiwnaorzmq, lucjygedpvsbhftkxipnaogzmb, luxjygjdpvsbhltkxiwnaorzmq, lucxygedpvsbhftkxzwnaorjmq, luajygedpvsbhftzxiwaaorzmq, lhcjygedpvsqhftfxiwnaorzmq, lucjygecphsbhftkxiwnaprzmq, lucjygedpvsbhptkxifnaorqmq, lucjygedpvichftkpiwnaorzmq, lucjygedpcsbhstkxswnaorzmq, kucjygedpvsbhftkxiwbyorzmq, lfpjxgedpvsbhftkxiwnaorzmq, lucjytldpvsbhftkxiwdaorzmq, lufjygedpvfbhftbxiwnaorzmq, lucjygebpvgbhftkxipnaorzmq, luujygedpvdbhftkxiwnaorzmd, lucjygedpvsbhfbyxwwnaorzmq, lucjygedpvsbhftkxiwnaoqpmw, qucgygedpvsbhftkxiwnaortmq, ludjtgedpvsbhftkxiunaorzmq, lucjyiedovsbhftkxiwjaorzmq, lucjygedpysbjftoxiwnaorzmq, lumjygedpvsbuftkxiknaorzmq, lucjygedpvsbhfokxgonaorzmq, lucjygeqpvsbhftkfiwnaorzeq, lucjygedpvskhftkxiwntorkmq, luujygedpvsbhftkxiwraorzmt, lucwygedpvsbjftkxiwnaorzmj, jucjyfedcvsbhftkxiwnaorzmq, luujygedpnsehftkxiwnaorzmq, lucjygedpvszhfckxiwnaorzmi, lucjyredpvsbzftkpiwnaorzmq, lucjygedpvsbwfgkxiwnaorzoq, lucjygedpvgbhftkpiwnaorzms, lucjygedpvjbhftkxzwnaoizmq, vucjycedpvsbhftkxiwfaorzmq, luawygeapvsbhftkxiwnaorzmq, lucjygetpvsbhftkxiwnaafzmq, lucjvgedpvsbhftkxywnavrzmq, luolygedpvsbgftkxiwnaorzmq, likjygedpvsbhftkxiwnabrzmq, lucjygedovsbhftkxirpaorzmq, lucjygedphsshftkxqwnaorzmq, uuqjygewpvsbhftkxiwnaorzmq, lucjygedcvsbhftkxiwoarrzmq, lucnygedpvsbhfakxiwnaorzms, lucjygedpvsbhntkxiwnawrzmb, lucjygedpvsblfxkxivnaorzmq, lucjygedpvsghftkxiwnaawzmq, yucjygedpgsbhftkxiwnaorzbq, lucjyweapvsbhftkxiwnaoezmq, lucjygevpvsbyftcxiwnaorzmq, luejygedovsbhftkxiwnqorzmq, lucjyqedpvsbhfbkxiwnaorzms, lucjypedpvsbhftwxiwnhorzmq, lucjygedpvsbhmtkviwxaorzmq, lucjogedpvpbhftkxiwnaorqmq, lucjygedpvsbhztkxkwnaoazmq, lucjyaedpvsbcftkxiwnaorzhq, lucjygbdpvkbhftkxiznaorzmq, lucpygedpvzbhftkxfwnaorzmq, lucjmgedpcsbhftkxiwnaoezmq, lucjygedyvsbbftkxiwnnorzmq, lucjyyedpvsbhftuxiwnaonzmq, lucjygfdpvsbhutkxiwnaorzmt, uccjygedpvschftkxiwnaorzmq, lusjygedpvbbhqtkxiwnaorzmq, ducuygedpvsbhftkxiwnaorzyq, lucjygkdvwsbhftkxiwnaorzmq, cucjyyedpvsbhftkxiwnaerzmq, lucjygedavsbhftkxiwnkorzbq, lucjygedmvsyhftkxiwiaorzmq, lucjygeipvsbhfpkxiwnaorzpq, vucjugedvvsbhftkxiwnaorzmq, lucjyzedpvsbhftkxpwnaoozmq, lucjygedpvgbhftkxiwtaorzqq, lecjygedpvcwhftkxiwnaorzmq, lucjyghdpvsbhfcyxiwnaorzmq, lucjygedpvesqftkxiwnaorzmq, lucjyjehpvsbhftbxiwnaorzmq, lucjygedpvtbhdtkxignaorzmq, lucjygxdpgsbhftkxivnaorzmq, lucjygvdpvsbhftkpiwnaorzqq, lucjysedpvsbhftkxiwnalrzmc, lucjygedpvkbhjtkxiwnaorsmq, lucjygedpvsbvfgkxiwnaerzmq, lucjygedpvsihftkxilnaorzmu, lvcvygndpvsbhftkxiwnaorzmq, lucjysedpqsbhftkxiwnaordmq, lucsygeypvsbhftkwiwnaorzmq, lucjygewpotbhftkxiwnaorzmq, lucjysedpvsbhftkxiwnanrzmv, lucjygedpvsbhutkxiwnaoplmq, wucjygedpvsqbftkxiwnaorzmq, lacjygeepvsbhftkxiwnjorzmq, lucjygedpusyhftkxicnaorzmq, qucjyredpvsbhftkxiwnworzmq, lucjygedevsbhftkgiwnayrzmq, lucjygedpksbrftkliwnaorzmq, lucjygedpvsbhfgkxisnaorzeq, lucjygedpvhdhftkeiwnaorzmq, lucjsgedpvsboftkxiwnaorumq, luctygedpvsbhftouiwnaorzmq, lucjygedpvsjhfukjiwnaorzmq, lucjagrepvsbhftkxiwnaorzmq, lucjkgerpvsbhftkxiwnairzmq, turjygedpvsbnftkxiwnaorzmq, lbcjygedpvsbhftkdpwnaorzmq, lucpygedpvsbhftkxnwnoorzmq, jucjygedpvsbhbtkxicnaorzmq, lecjygedpvsbhftkriwnaogzmq, licjyvcdpvsbhftkxiwnaorzmq, lrcjygewpnsbhftkxiwnaorzmq, ltcxygedpvlbhftkxiwnaorzmq, luctygedpvhbhztkxiwnaorzmq, lucwygedplsbhfakxiwnaorzmq, lucjygedpnsbhftkxiwjaoezmq, lucpygedptsbhftkxiwnaorzmo, lucjygedpvibhqtkxiknaorzmq, lucjwgqdpvrbhftkxiwnaorzmq, lucjmgkdpvsbhftkxiwraorzmq, lucjygwupvsbhftkxiznaorzmq, lucjhgedpvobhftkxiwncorzmq, lucjygedpvsbhftkxiwnaohtmj, lucjygedpvsbeftkfiwnaorzyq, lucjygcdpvsbpftkhiwnaorzmq, lucjygedpmsbhftkxiwnkouzmq, oucjygedpvsbyftkximnaorzmq, lucjcgedpvsbhftkxywnforzmq, lfcjygedfvsbdftkxiwnaorzmq, ducjygedevsbhfttxiwnaorzmq, ldcjdgedpvsbhftkxiwnavrzmq, lucjymedmvsbhqtkxiwnaorzmq, lucjygedpvabhftkxiwnasrlmq, lucjygefpvsbhftkxmwnaorkmq"
str = str.split(", ")

for s in str:
    print("scanning {0}".format(s))
    for t in str:
        if differPosition(s,t) != -1:
            print(differPosition(s,t))
            print(s)
            print(t)
            exit()
print("end")


