# Ohjelmistotekniikka
---
### *Kurssin suoritettuaan opiskelija:*

- Tuntee ohjelmistotuotantoprosessin vaiheet
- On tietoinen vesiputousmallin ja ketterän ohjelmistotuotannon luonteesta
- Osaa soveltaa versionhallintaa osana ohjelmistokehitystä
- Osaa soveltaa UML-mallinnustekniikkaa ohjelmiston suunnittelussa ja dokumentoinnissa
- Tuntee ohjelmiston testauksen eri vaiheet
- Osaa soveltaa automatisoitua testausta yksinkertaisissa ohjelmistoprojekteissa. 
- Tuntee tärkeimpiä ohjelmiston suunnitteluperiaatteita ja osaa soveltaa niitä yksinkertaisissa projekteissa.

source: [link](https://ohjelmistotekniikka-hy.github.io/python/viikko1)

### Some important files :joy:

- [gitlog](https://github.com/matiasto/ot-harjoitustyo/blob/main/laskarit/viikko1/gitlog.txt)
- [komentorivi](https://github.com/matiasto/ot-harjoitustyo/blob/main/laskarit/viikko1/komentorivi.txt)

## ~~Esimerkki suoritus~~

>Using recursion

```python
def fizzbuzz(num):
    output = ""
    values = {3: "Fizz", 5: "Buzz", 7: "Fizz"}
    if num > 100:
        return False
    for value, word in values.items():
        if num % value == 0:
            output += word
    print(num )if output == "" else print(output)
    num += 1
    return fizzbuzz(num)

fizzbuzz(1)
```
testi