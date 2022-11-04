def validate(function):
    INPUTS = [
        "aaaaaaa",
        "Test. Also a test.",
        "Cambridge University Engineering Society",
        "Since they are still preserved in the rocks for us to see, they must have been formed quite recently, that is, geologically speaking. What can explain these striations and their common orientation? Did you ever hear about the Great Ice Age or the Pleistocene Epoch? Less than one million years ago, in fact, some 12,000 years ago, an ice sheet many thousands of feet thick rode over Burke Mountain in a southeastward direction. The many boulders frozen to the underside of the ice sheet tended to scratch the rocks over which they rode. The scratches or striations seen in the park rocks were caused by these attached boulders. The ice sheet also plucked and rounded Burke Mountain into the shape it possesses today.",
        "After hunting for several hours, we finally saw a large seal sunning itself on a flat rock. I took one of the wooden clubs while Larry took the longer one. We slowly snuck up behind the seal until we were close enough to club it over its head. The seal slumped over and died. This seal would help us survive. We could eat the meat and fat. The fat could be burned in a shell for light and the fur could be used to make a blanket. We declared our first day of hunting a great success.",
    ]
    EXP_OUTPUTS = [
        "AaAaAaA",
        "TeSt. AlSo A tEsT.",
        "CaMbRiDgE uNiVeRsItY eNgInEeRiNg SoCiEtY",
        "SiNcE tHeY aRe StIlL pReSeRvEd In ThE rOcKs FoR uS tO sEe, ThEy MuSt HaVe BeEn FoRmEd QuItE rEcEnTlY, tHaT iS, gEoLoGiCaLlY sPeAkInG. wHaT cAn ExPlAiN tHeSe StRiAtIoNs AnD tHeIr CoMmOn OrIeNtAtIoN? dId YoU eVeR hEaR aBoUt ThE gReAt IcE aGe Or ThE pLeIsToCeNe EpOcH? lEsS tHaN oNe MiLlIoN yEaRs AgO, iN fAcT, sOmE 12,000 yEaRs AgO, aN iCe ShEeT mAnY tHoUsAnDs Of FeEt ThIcK rOdE oVeR bUrKe MoUnTaIn In A sOuThEaStWaRd DiReCtIoN. tHe MaNy BoUlDeRs FrOzEn To ThE uNdErSiDe Of ThE iCe ShEeT tEnDeD tO sCrAtCh ThE rOcKs OvEr WhIcH tHeY rOdE. tHe ScRaTcHeS oR sTrIaTiOnS sEeN iN tHe PaRk RoCkS wErE cAuSeD bY tHeSe AtTaChEd BoUlDeRs. ThE iCe ShEeT aLsO pLuCkEd AnD rOuNdEd BuRkE mOuNtAiN iNtO tHe ShApE iT pOsSeSsEs ToDaY.",
        "AfTeR hUnTiNg FoR sEvErAl HoUrS, wE fInAlLy SaW a LaRgE sEaL sUnNiNg ItSeLf On A fLaT rOcK. i ToOk OnE oF tHe WoOdEn ClUbS wHiLe LaRrY tOoK tHe LoNgEr OnE. wE sLoWlY sNuCk Up BeHiNd ThE sEaL uNtIl We WeRe ClOsE eNoUgH tO cLuB iT oVeR iTs HeAd. ThE sEaL sLuMpEd OvEr AnD dIeD. tHiS sEaL wOuLd HeLp Us SuRvIvE. wE cOuLd EaT tHe MeAt AnD fAt. ThE fAt CoUlD bE bUrNeD iN a ShElL fOr LiGhT aNd ThE fUr CoUlD bE uSeD tO mAkE a BlAnKeT. wE dEcLaReD oUr FiRsT dAy Of HuNtInG a GrEaT sUcCeSs.",    
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, str), "Function did not return string"
        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')