# Russian latiniser | Latinizator russkogo jazyka

## EN

This is a package of several functions to implement transliteration of words in texts written in russian cyrillics into
new custom system of the latin script.

More information about new script, as well as implemented functions of this package, can be found on the
website http://russianlatiniser.pythonanywhere.com/. (ru)

## RU

Eto pakêt iz nêskoljkih funkcij dlâ translitêracii slow i têkstow, napisannyh russkoj kirillicej, w
nowuju sistêmu latinskogo šrifta.

Bolêje podrobnuju informaciju o nowoj sistêmê pisjma, a takže rêalizaciju funkcij dannogo pakêta možno najti na
sajtê http://russianlatiniser.pythonanywhere.com/.

## Implementation

You need only one function to translate any string to latin script:
```python
from russian_latiniser import RussianLatiniser

latiniser = RussianLatiniser()
res = latiniser.transliterate_cyrillics_to_latin("Мороз и солнце, день чудесный...")
print(res) # Output: Moroz i solnce, dênj čudêsnyj...
```