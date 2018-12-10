---
title: IchSagNurWeb
description: Cheating on a riddle with brute force.
---

Recently, I was asked if I could figure out which single word "Ich sag nur Web" stands for when rearranging the letters (German for "I just say web"). I tried but I couldn't come up with the solution. Since I was too proud to give up, I employed some automated cheating.

The idea was to simply generate each permutation of the letters and check which of them are valid German words. This requires testing `12! = 479 001 600` words which would take a *very* long time. Fortunately, we can use the fact that in German the letter "c" almost exclusively occurs within the sequence "ch" or "sch" to reduce the search space.

In the case of "sch", we only need to permutate the remaining letters "iagnurweb" and insert "sch" at each position in the permutations. This reduces to `10 * 9! = 10! = 3 628 800` words to test, two orders of magnitude smaller. For "ch" it would be `11! = 39 916 800` words.

## Code

For Python, I found the [`pyenchant`](https://github.com/rfk/pyenchant) spell-checking library which I used to check for valid German words. Since the number of permutations is quite large, I offloaded it to multiple processes.

{% highlight python %}
from itertools import permutations
from multiprocessing import Pool
import enchant

riddle = "ichsagnurweb"
sch = "sch"
german_dictionary = enchant.Dict("de_DE")

def check(permutation):
    permutation = "".join(permutation)
    for i in range(len(permutation) + 1):
        word = permutation[:i] + sch + permutation[i:]
        word = word.capitalize()
        if german_dictionary.check(word):
            print(word)

def main():
    characters = set(riddle) - set(sch)
    perms = permutations(characters)
    # Parallelize work
    workers = Pool()
    workers.imap(check, perms, chunksize=50000)
    workers.close()
    workers.join()

main()
{% endhighlight %}

## Results

After about two minutes on my machine, the "sch" version spit out the following words. Some of the words are hilarious and some aren't even real words. The only real candidate on the list is **Braunschweig**, a city in Germany. Riddle solved!

    Arschweinbug
    Barschwungei
    Bauschwinger
    Bierwaschgnu
    Bierwaschung
    Braugenwisch
    Braunschweig
    Braunwegschi
    Buschwegiran
    Buschwegrain
    Einwaschburg
    Erbschwingau
    Genbrauwisch
    Genraubwisch
    Grabneuwisch
    Grabwunschei
    Neugrabwisch
    Raubgenwisch
    Schubwegiran
    Schubwegrain
    Schwingbauer
    Schwingbraue
    Schwingerbau
    Schwungbarei
    Waschbiergnu
    Wascheinburg
    Waschreibung
    Wegbraunschi
    Wegbuschiran
    Wegbuschrain
    Wegschubiran
    Wegschubrain
    Weinarschbug
    Wunschgrabei

For fun, I also ran the "ch" version. It took about 25 minutes to generate the following:

    Achsburgwein
    Achsburgwien
    Achswegrubin
    Achsweinburg
    Arschweinbug
    Bachwegruins
    Bachwegurins
    Barschwungei
    Barweichgnus
    Bauchingwers
    Bauschwinger
    Beirangwuchs
    Bierwachgnus
    Bierwachsgnu
    Bierwaschgnu
    Bierwaschung
    Braugenwisch
    Braunschweig
    Braunwegschi
    Bruchgaswein
    Bruchgaswien
    Bruchweganis
    Bruchweingas
    Buchgraswein
    Buchgraswien
    Buchsargwein
    Buchsargwien
    Buchsingware
    Buchwagensir
    Buchwagensri
    Buchwarnsieg
    Buchwegrains
    Buchweingras
    Buchweinsarg
    Burgachswein
    Burgachswien
    Burgeinwachs
    Burgnachweis
    Burgsachwein
    Burgsachwien
    Burgwachsein
    Burgweichsan
    Buschwegiran
    Buschwegrain
    Busringwache
    Buswachniger
    Busweichgarn
    Busweichrang
    Eichwarnbugs
    Einburgwachs
    Eingrabwuchs
    Einwachsburg
    Einwaschburg
    Erbschwingau
    Gasbruchwein
    Gasbruchwien
    Gasweinbruch
    Genbrauwisch
    Genraubwisch
    Grabeinwuchs
    Grabneuwisch
    Grabsuchwein
    Grabsuchwien
    Grabwunschei
    Grasbuchwein
    Grasbuchwien
    Grasweinbuch
    Nachweisburg
    Neugrabwisch
    Rangbeiwuchs
    Rangsuchweib
    Rangweichbus
    Raubgenwisch
    Ringbuswache
    Ringsubwache
    Ringsuchwabe
    Sachburgwein
    Sachburgwien
    Sachwegrubin
    Sachweinburg
    Sargbuchwein
    Sargbuchwien
    Sargweinbuch
    Schubwegiran
    Schubwegrain
    Schwingbauer
    Schwingbraue
    Schwingerbau
    Schwungbarei
    Singbuchware
    Subringwache
    Subwachniger
    Subweichgarn
    Subweichrang
    Suchgrabwein
    Suchgrabwien
    Suchrangweib
    Suchringwabe
    Suchweingrab
    Wachbiergnus
    Wachburgsein
    Wachbusniger
    Wachsbiergnu
    Wachseinburg
    Wachsreibung
    Wachsubniger
    Wagenbuchsir
    Wagenbuchsri
    Warnbuchsieg
    Warneichbugs
    Waschbiergnu
    Wascheinburg
    Waschreibung
    Wegachsrubin
    Wegbachruins
    Wegbachurins
    Wegbraunschi
    Wegbruchanis
    Wegbuchrains
    Wegbuschiran
    Wegbuschrain
    Wegsachrubin
    Wegschubiran
    Wegschubrain
    Weichbargnus
    Weichburgsan
    Weichbusgarn
    Weichbusrang
    Weichrangbus
    Weichsubgarn
    Weichsubrang
    Weinachsburg
    Weinarschbug
    Weinbruchgas
    Weinbuchgras
    Weinbuchsarg
    Weingasbruch
    Weingrasbuch
    Weinsachburg
    Weinsargbuch
    Weinsuchgrab
    Wunschgrabei