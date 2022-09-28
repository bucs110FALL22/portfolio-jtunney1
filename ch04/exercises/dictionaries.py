article_text = "The official campaign arm of Senate Republicans has been running attack ads that mislead viewers about how a law signed by President Joe Biden in August will affect seniors enrolled in Medicare. One of the National Republican Senatorial Committee ads shows a senior sitting alone, looking sad, as a narrator claims Democratic Sen. Raphael Warnock of Georgia supported “deep cuts in Medicare spending.” A second ad shows a senior receiving help moving his legs as the narrator claims, “Warnock voted with Biden to slash Medicare spending.” A third ad features a claim that Democratic Sen. Mark Kelly of Arizona “went along with nearly $300 billion less in Medicare spending for seniors.” Small text in all three ads makes clear that these Medicare claims are about Warnock and Kelly voting for the Inflation Reduction Act, the major health care, climate and tax law that squeaked through the Senate thanks to Vice President Kamala Harris’ tiebreaking vote. But experts on Medicare say that the ads deceptively depict that law. Facts First: While the Inflation Reduction Act is expected to reduce Medicare prescription drug spending by the federal government, that’s because the law will allow the government to spend less money to buy medications from pharmaceutical companies – not because the law will cut the benefits received by seniors enrolled in Medicare. In reality, the law makes Medicare substantially more generous to seniors. Stacie Dusetzina, associate professor of health policy at the Vanderbilt University School of Medicine, called the ads “very misleading.” She said in an email: “Essentially, the Inflation Reduction Act improves access to prescription drugs for Medicare beneficiaries by lowering what Medicare pays for prescription drugs. Framing this as a ‘cut’ to benefits is nonsense.” Juliette Cubanski, deputy director of the Medicare policy program at the Kaiser Family Foundation, a nonprofit that studies health policy, also said that reducing Medicare spending “is not the same thing as cutting Medicare benefits” and “Medicare beneficiaries, especially those with high drug costs, stand to benefit” from the changes made by the Inflation Reduction Act. Cubanski said in an email: “In fact, the law actually improved Medicare’s drug benefit by tackling high drug prices, a longstanding concern for people with Medicare, and capping what Medicare beneficiaries pay out of pocket for prescription drugs, along with other drug benefit improvements, like free vaccines and capping insulin copays.” And Gerard Anderson, a professor and health policy expert at the Johns Hopkins University Bloomberg School of Public Health, said that when the ads portray the Inflation Reduction Act as a law that imposes costs on Medicare beneficiaries, “what they really mean is that the pharmaceutical companies will get fewer dollars.” Similar Republican claims have been fact-checked earlier this year by other outlets, including PolitiFact and The Washington Post. A spokesperson for the National Republican Senatorial Committee did not respond to a CNN request for comment this week."

dictonary = {
    "white house":"Pit of Despair",
    "allegedly":"totally",
    "bill":"snap I didn’t screenshot",
    "official":"puppy",
    "congressional":"spaaaaace",
    "Eepublican":"piano accordionist",
    "Democrat":"chromatic button accordionist",
    "Senator": "magical wizard",
    "representative": "unmagical wizard",
    "Secretary":"eating champion",
    "leaders":"goblins",
    "Washington":"Mount Doom",
    "President": "you know, the guy"
}

for word, value in dictonary.items():
    article = article_text.replace(word, value)

print(article)