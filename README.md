# 3η Εργασία Αρχιτεκτονικής Προηγμένων Υπολογιστών
_του Βασιλείου Μπεσλεμέ και του Διονυσίου Δανιήλ Πλέσσα_<br>
[vampesle@ece.auth.gr](mailto:vampesle@ece.auth.gr), [dplessas@ece.auth.gr](mailto:dplessas@ece.auth.gr)<br>
9862, 9768

-------------------------------------------

## Βήμα 1ο

### 1.
Σύμφωνα με το [αρχικό paper](https://www.hpl.hp.com/research/mcpat/micro09.pdf), η επικύρωση των αποτελεσμάτων του McPAT έγινε με τη σύγκρισή τους με δημοσιευμένα δεδομένα για τους επεξεργαστές:
* SPARC Niagara (90nm, 1.2GHz, 1.2V)
* SPARC Niagara2 (65nm, 1.4GHz, 1.1V)
* Intel Xeon (65nm, 3.4GHz, 1.25V)
* Alpha 21364 (180nm, 1.2GHz, 1.5V)

Τα δεδομένα που χρησιμοποιήθηκαν, εκτός των άλλων, περιλαμβάνουν το ρυθμό ρολογιού, θερμοκρασίες λειτουργίας καθώς και άλλες αρχιτεκτονικές παραμέτρους.

Μελετήθηκαν η απόλυτη και η σχετική ακρίβεια των αποτελεσμάτων, τα οποία, εν τέλει, είναι αρκετά κοντά στα δημοσιευμένα δεδομένα.


### 2.
Υπάρχουν τρεις ισχύες οι οποίες απαρτίζουν τη συνολική ισχύ που καταναλώνει ένας επεξεργαστής, και αυτές είναι:
* Dynamic power: η δυναμική ισχύς είναι το άθροισμα δύο επιμέρους ισχύων, των:
	- Switching power: η ισχύς που καταναλώνεται στη φόρτιση/εκφόρτιση χωρητικοτήτων, όπως για παράδειγμα πυκνωτών αλλά και των πυλών MOSFETs.
	- Short-circuit power: η ισχύς που καταναλώνεται κατά το στιγμιαίο βραχυκύκλωμα της τάσης τροφοδοσίας με την γείωση, καθώς ένα MOSFET αλλάζει κατάσταση.
* Static/leakage power: η ισχύς που καταναλώνεται από ρεύματα διαρροών, π.χ. DC ρεύματα ανάστροφης πόλωσης διόδων, διαρροής πυκνωτών, διαρροής πύλης-πηγής (Igss) και διαρροής εκροής-πηγής (Ιdss) των MOSFETs.

<font size="2">
Αρκετά ενδιαφέρον είναι το γεγονός ότι σε αρχιτεκτονικές μικρότερες των 90nm, η ισχύς διαρροής υπερέχει των άλλων τύπων ισχύων, ενώ σε μεγαλύτερες των 90nm, η ισχύς switching είναι αυτή που ευθύνεται για την κατανάλωση του μεγαλύτερου ποσοστού της ενέργειας. 
</font>

Κατά την εκτέλεση διαφορετικών προγραμμάτων, θα αναμέναμε το πιο "βαρύ" πρόγραμμα, δηλαδή αυτό που χρησιμοποιεί τον επεξεργαστή για μεγαλύτερο χρονικό διάστημα (μεγαλύτερο CPU time), να καταναλώνει μεγαλύτερη δυναμική ισχύ, αφού οδηγεί τα transistors του επεξεργαστή σε περισσότερες εναλλαγές κατάστασης. Από την άλλη, όσο μεγαλύτερο χρόνο εκτέλεσης έχει ένα πρόγραμμα (χωρίς να αυξάνεται απαραίτητα το CPU time, όπως για παράδειγμα στις καθυστερήσεις που οφείλονται στα περιφερειακά και την αλληλεπίδραση του χρήστη), τόσο αυξάνεται η ισχύς διαρροής, η οποία είναι κυρίαρχη για επεξεργαστές με transistors μικρότερου μεγέθους.


### 3.
Στην περίπτωση που στόχος της συσκευής είναι η εκτέλεση μιας συγκεκριμένης διεργασίας, ύστερα από την οποία ο επεξεργαστής θα αδρανοποιείται, τη μεγαλύτερη διάρκεια ζωής μπαταρίας θα έχει η συσκευή με τον πιο ενεργειακά αποδοτικό επεξεργαστή, δηλαδή αυτόν που μπορεί να παρέχει μεγαλύτερη υπολογιστική ισχύ ανά μονάδα ενέργειας. Το τελευταίο είναι ένα κριτήριο που δεν εξαρτάται από το TDP (thermal power design) της CPU. Σε περίπτωση που η χρήση του συστήματος επαφίεται στον χρήστη (όπως γίνεται με τους προσωπικούς υπολογιστές), ο οποίος συχνά επιλέγει πιο απαιτητικό λογισμικό, ανάλογα με τις δυνατότητες του συστήματος που διαθέτει, η επιλογή του δεύτερου επεξεργαστή ενδεχομένως να οδηγούσε σε μικρότερη διάρκεια μπαταρίας, παρά το γεγονός ότι μπορεί να είναι πιο αποδοτικός.

To McPAT από μόνο του, δεν είναι αρκετό για να αποφασίσουμε για την ενεργειακή αποδοτικότητα ενός επεξεργαστή. Για το τελευταίο, θα μας ήταν απαραίτητο να γνωρίζουμε και το χρόνο εκτέλεσης ενός benchmark για παράδειγμα, ώστε να υπολογίσουμε ένα μέγεθος όπως το PDP (Power Delay Product) ή το EDP (Energy Delay Product), το οποίο θα ήταν ενδεικτικό της ενεργειακής αποδοτικότητας του συστήματος. Τέτοια δεδομένα, θα μπορούσαμε να εξάγουμε από τον προσομοιωτή Gem5 για παράδειγμα.


### 4.
Παρατηρώντας τα αποτελέσματα του McPAT για τους δύο επεξεργαστές, προκύπτει ότι η ισχύς διαρροής του Xeon (36.832W) είναι αρκετά μεγαλύτερη από αυτή του A9 (0.109W). Δεδομένου ότι το πρόγραμμα τρέχει 40 φορές πιο γρήγορα στον Xeon, υπολογίζουμε ότι η ελάχιστη δυνατή ενέργεια που απαιτείται για την εκτέλεση του προγράμματος είναι `36.832 * (1 / 40) = 0.921` (μονάδες χρόνου *W), ενώ για τον A9 `0.109 * 1 = 0.109` (μονάδες χρόνου *W).

Στους παραπάνω υπολογισμούς, χρησιμοποιήσαμε μόνο την ισχύ διαρροής, αφού αυτή, σε αντίθεση με τη δυναμική ισχύ, δεν επηρεάζεται από το είδος του προγράμματος που εκτελείται και επειδή είναι η μόνη μορφή ισχύος που καταναλώνεται ακόμα και αν ο επεξεργαστής είναι σε αδράνεια. Ωστόσο, η CPU Xeon θα μπορούσε να έχει αρκετά μικρότερη δυναμική ισχύ από την A9 και να ανατρέπει τελικά το αποτέλεσμα (για ένα συγκεκριμένο χρονικό παράθυρο, όπου η μεγαλύτερη ισχύς διαρροής του Xeon δε θα ανέτρεπε, ξανά, το αποτέλεσμα). Πραγματοποιώντας τους ίδιους υπολογισμούς, χρησιμοποιώντας τη δυναμική ισχύ αυτή τη φορά, καταλήγουμε στο ίδιο συμπέρασμα. Επομένως, ανεξάρτητα από το πρόγραμμα που χρησιμοποιείται, θα μπορούσαμε να πούμε ότι ο Α9 είναι πιο ενεργειακά αποδοτικός, παρότι είναι αρκετά πιο αργός από τον Intel Xeon.

[Πηγή](https://semiengineering.com/knowledge_centers/low-power/low-power-design/power-consumption/)

## Βήμα 2ο

### 1.

Το energy υπολογίζεται με ολοκλήρωση της ισχύος στον χρόνο εκτέλεσης. Χρησιμοποιήσαμε το print_energy.py που υπολογίζει το energy πολλαπλασιάζοντας τον χρόνο εκτέλεσης με το άθροισμα δυναμικής και ισχύος διαρροής: ` energy = (leakage + dynamic)*runtime `. Το runtime προέρχεται από τα αποτελέσματα των προσομοιώσεων του gem5 ενώ τα leakage και dynamic προέρχονται από τα αποτελέσματα του McPat.

### 2.

Αποτελέσματα
------------

Οι προσομοιώσεις που εκτελέστηκαν είναι για τα παρακάτω συστήματα:
|Num.	| Τitle | L1d size (KB) | L1d Assoc. | L1i size (KB) | L1i Assoc. | L2 size	 (KB) | L2 Assoc.  | Cache Line (B) |
| ------ | ----- | --------- | ------------- | --------- |------------- | --------- | ------------- | --------- | 
| **1** | **Control** | 256 | 1 | 256 | 1 | 4096 | 1 | 64 |
| **2** | L1 Alloc. Test | 128 | 1 | 256 | 1 | 4096 | 1 | 64 |
| **3** | L1 Alloc. Test | 256 | 1 | 128 | 1 | 4096 | 1 | 64 |
| **4** | L2 Test | 256 | 1 | 256 | 1 | 2048 | 1 | 64 |
| **5** | L2 Test | 256 | 1 | 256 | 1 | 1024 | 1 | 64 |
| **6** | L1d Test | 512 | 1 | 256 | 1 | 4096 | 1 | 64 |
| **7** | C. Line Test | 256 | 1 | 256 | 1 | 4096 | 1 | 32 |
| **8** | C. Line Test | 256 | 1 | 256 | 1 | 4096 | 1 | 128|
| **9** | Assoc. Test | 256 | 2 | 256 | 2 | 4096 | 2 | 64 |
| **10**| Assoc. Test | 256 | 4 | 256 | 2 | 4096 | 4 | 64 |
| **11**| Assoc. Test | 256 | 8 | 256 | 8 | 4096 | 8 | 64 |
| **12**| Perfect Test | 256 | 4 | 256 | 4 | 4096 | 4 | 128 |
| **13**| Perfect Final | 256 | 4 | 256 | 4 | 4096 | 4 | 256 |
| **14** | **Ideal** | 64 | 4 | 64 | 4 | 1024 | 4 | 256 |
| **15** | **IdealNew** | 128 | 2 | 128 | 2 | 1024 | 2 | 32 |

Τα συστήματα 1 έως 12 είναι τα δοκιμαστικά συστήματα από το δεύτερο μέρος της προηγούμενης άσκησης, το σύστημα 13 είναι το μέγιστων επιδόσεων ανεξαρτήτου κόστους ενώ το  σύστημα 14 είναι το ιδανικό σύστημα που επιλέξαμε με την συνάρτηση κόστους που υλοποιήσαμε.

Machine 1
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.53747      |  1.13880     |  1.18263     |  7.05754      |  2.62833      |
|**Energy**           | 479.262916mJ | 353.673161mJ| 374.025984mJ| 2029.421792mJ| 772.186533mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 17.5954mm2  | 17.5954mm2 | 17.5954mm2 | 17.5954mm2  | 17.5954mm2  |
|**Subthreshold Leakage**| 2.50962W     | 2.50962W    | 2.50962W    | 2.50962W     | 2.50962W     |
|**Gate Leakage**     | 0.0189625W   | 0.0189625W  | 0.0189625W  | 0.0189625W   | 0.0189625W   |
|**Runtime Dynamic**  | 0.499585W    | 0.500981W   | 0.559397W   | 0.207781W    | 0.297759W    |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 12.8813mm2  | 12.8813mm2 | 12.8813mm2 | 12.8813mm2  | 12.8813mm2  |
|**Subthreshold Leakage**| 0.00886875W  | 0.00886875W | 0.00886875W | 0.00886875W  | 0.00886875W  |
|**Gate Leakage**     | 0.00107422W  | 0.00107422W | 0.00107422W | 0.00107422W  | 0.00107422W  |
|**Runtime Dynamic**  | 0.0104672W   | 0.000868803W| 0.00024668W | 0.025636W    | 0.0079842W   |

Machine 2
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.59488      |  1.13756     |  1.18990     |  7.05754      |  2.63117      |
|**Energy**           | 448.583068mJ | 319.200019mJ| 340.093648mJ| 1847.874082mJ| 702.117716mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 15.9377mm2  | 15.9377mm2 | 15.9377mm2 | 15.9377mm2  | 15.9377mm2  |
|**Subthreshold Leakage**| 2.28171W     | 2.28171W    | 2.28171W    | 2.28171W     | 2.28171W     |
|**Gate Leakage**     | 0.0173334W   | 0.0173334W  | 0.0173334W  | 0.0173334W   | 0.0173334W   |
|**Runtime Dynamic**  | 0.415802W    | 0.430686W   | 0.48201W    | 0.18007W     | 0.257798W    |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 12.8813mm2  | 12.8813mm2 | 12.8813mm2 | 12.8813mm2  | 12.8813mm2  |
|**Subthreshold Leakage**| 0.00886875W  | 0.00886875W | 0.00886875W | 0.00886875W  | 0.00886875W  |
|**Gate Leakage**     | 0.00107422W  | 0.00107422W | 0.00107422W | 0.00107422W  | 0.00107422W  |
|**Runtime Dynamic**  | 0.0193497W   | 0.00107155W | 0.00270827W | 0.0256472W   | 0.0080438W   |

Machine 3
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.53748      |  1.13559     |  1.18263     |  7.05756      |  2.62833      |
|**Energy**           | 443.974563mJ | 325.841879mJ| 346.879665mJ| 1867.427376mJ| 714.836635mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 16.0884mm2  | 16.0884mm2 | 16.0884mm2 | 16.0884mm2  | 16.0884mm2  |
|**Subthreshold Leakage**| 2.28171W     | 2.28171W    | 2.28171W    | 2.28171W     | 2.28171W     |
|**Gate Leakage**     | 0.0173334W   | 0.0173334W  | 0.0173334W  | 0.0173334W   | 0.0173334W   |
|**Runtime Dynamic**  | 0.499582W    | 0.493406W   | 0.559389W   | 0.20778W     | 0.297759W    |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 12.8813mm2  | 12.8813mm2 | 12.8813mm2 | 12.8813mm2  | 12.8813mm2  |
|**Subthreshold Leakage**| 0.00886875W  | 0.00886875W | 0.00886875W | 0.00886875W  | 0.00886875W  |
|**Gate Leakage**     | 0.00107422W  | 0.00107422W | 0.00107422W | 0.00107422W  | 0.00107422W  |
|**Runtime Dynamic**  | 0.0104686W   | 0.00170562W | 0.000254125W| 0.0256361W   | 0.0193248W   |

Machine 4
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.56092      |  1.13766     |  1.18262     |  7.05935      |  2.63077      |
|**Energy**           | 484.395309mJ | 351.834552mJ| 373.450192mJ| 2023.243595mJ| 771.599882mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 17.5954mm2  | 17.5954mm2 | 17.5954mm2 | 17.5954mm2  | 17.5954mm2  |
|**Subthreshold Leakage**| 2.50962W     | 2.50962W    | 2.50962W    | 2.50962W     | 2.50962W     |
|**Gate Leakage**     | 0.0189625W   | 0.0189625W  | 0.0189625W  | 0.0189625W   | 0.0189625W   |
|**Runtime Dynamic**  | 0.492039W    | 0.492507W   | 0.559402W   | 0.207727W    | 0.297483W    |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 7.47733mm2  | 7.47733mm2 | 7.47733mm2 | 7.47733mm2  | 7.47733mm2  |
|**Subthreshold Leakage**| 0.00460747W  | 0.00460747W | 0.00460747W | 0.00460747W  | 0.00460747W  |
|**Gate Leakage**     | 0.000556536W | 0.000556536W| 0.000556536W| 0.000556536W | 0.000556536W |
|**Runtime Dynamic**  | 0.0074136W   | 0.000731789W| 0.000178734W| 0.0208712W   | 0.00777041W  |

Machine 5
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.57986      |  1.13940     |  1.18262     |  7.06012      |  2.63262      |
|**Energy**           | 488.872194mJ | 352.090438mJ| 373.205506mJ| 2019.207734mJ| 771.564619mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 17.5954mm2  | 17.5954mm2 | 17.5954mm2 | 17.5954mm2  | 17.5954mm2  |
|**Subthreshold Leakage**| 2.50962W     | 2.50962W    | 2.50962W    | 2.50962W     | 2.50962W     |
|**Gate Leakage**     | 0.0189625W   | 0.0189625W  | 0.0189625W  | 0.0189625W   | 0.0189625W   |
|**Runtime Dynamic**  | 0.486153W    | 0.491757W   | 0.559402W   | 0.207705W    | 0.297274W    |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 4.17438mm2  | 4.17438mm2 | 4.17438mm2 | 4.17438mm2  | 4.17438mm2  |
|**Subthreshold Leakage**| 0.00275444W  | 0.00275444W | 0.00275444W | 0.00275444W  | 0.00275444W  |
|**Gate Leakage**     | 0.000392649W | 0.000392649W| 0.000392649W| 0.000392649W | 0.000392649W |
|**Runtime Dynamic**  | 0.00532681W  | 0.000648279W| 0.000120289W| 0.0168171W   | 0.00764785W  |

Machine 6
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.52644      |  1.13392     |  1.18216     |  7.03832      |  2.62712      |
|**Energy**           | 565.397385mJ | 417.055032mJ| 444.178980mJ| 2391.223349mJ| 912.449275mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 23.8415mm2  | 23.8415mm2 | 23.8415mm2 | 23.8415mm2  | 23.8415mm2  |
|**Subthreshold Leakage**| 2.96773W     | 2.96773W    | 2.96773W    | 2.96773W     | 2.96773W     |
|**Gate Leakage**     | 0.022475W    | 0.022475W   | 0.022475W   | 0.022475W    | 0.022475W    |
|**Runtime Dynamic**  | 0.627496W    | 0.611864W   | 0.69253W    | 0.268131W    | 0.371406W    |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 12.8813mm2  | 12.8813mm2 | 12.8813mm2 | 12.8813mm2  | 12.8813mm2  |
|**Subthreshold Leakage**| 0.00886875W  | 0.00886875W | 0.00886875W | 0.00886875W  | 0.00886875W  |
|**Gate Leakage**     | 0.00107422W  | 0.00107422W | 0.00107422W | 0.00107422W  | 0.00107422W  |
|**Runtime Dynamic**  | 0.00768571W  | 0.00067579W | 0.000166747W| 0.0254449W   | 0.00793762W  |

Machine 7
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.63820      |  1.15266     |  1.18598     | 11.66498      |  3.91979      |
|**Energy**           | 330.179210mJ | 234.703784mJ| 244.071482mJ| 2186.346204mJ| 747.404782mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 16.0588mm2  | 16.0588mm2 | 16.0588mm2 | 16.0588mm2  | 16.0588mm2  |
|**Subthreshold Leakage**| 1.66546W     | 1.66546W    | 1.66546W    | 1.66546W     | 1.66546W     |
|**Gate Leakage**     | 0.0113064W   | 0.0113064W  | 0.0113064W  | 0.0113064W   | 0.0113064W   |
|**Runtime Dynamic**  | 0.252279W    | 0.28372W    | 0.307516W   | 0.0711894W   | 0.112725W    |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 13.211mm2   | 13.211mm2  | 13.211mm2  | 13.211mm2   | 13.211mm2   |
|**Subthreshold Leakage**| 0.00816516W  | 0.00816516W | 0.00816516W | 0.00816516W  | 0.00816516W  |
|**Gate Leakage**     | 0.000776381W | 0.000776381W| 0.000776381W| 0.000776381W | 0.000776381W |
|**Runtime Dynamic**  | 0.00626062W  | 0.0005893W  | 0.000165917W| 0.00554513W  | 0.00464186W  |

Machine 8
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.53311      |  1.11498     |  1.17817     |  5.01106      |  1.99147      |
|**Energy**           | 1004.262590mJ| 720.447672mJ| 783.488522mJ| 3025.861934mJ| 1244.418099mJ|
|**Core Data**        |               |              |              |               |               |
|**Area**             | 36.1509mm2  | 36.1509mm2 | 36.1509mm2 | 36.1509mm2  | 36.1509mm2  |
|**Subthreshold Leakage**| 5.1311W      | 5.1311W     | 5.1311W     | 5.1311W      | 5.1311W      |
|**Gate Leakage**     | 0.0422332W   | 0.0422332W  | 0.0422332W  | 0.0422332W   | 0.0422332W   |
|**Runtime Dynamic**  | 1.27123W     | 1.20803W    | 1.3984W     | 0.711896W    | 0.96084W     |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 18.1823mm2  | 18.1823mm2 | 18.1823mm2 | 18.1823mm2  | 18.1823mm2  |
|**Subthreshold Leakage**| 0.0116336W   | 0.0116336W  | 0.0116336W  | 0.0116336W   | 0.0116336W   |
|**Gate Leakage**     | 0.00178194W  | 0.00178194W | 0.00178194W | 0.00178194W  | 0.00178194W  |
|**Runtime Dynamic**  | 0.0253606W   | 0.00193643W | 0.000437962W| 0.0477418W   | 0.0174254W   |

Machine 9
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.53477      |  1.13403     |  1.18143     |  7.03840      |  2.62076      |
|**Energy**           | 479.634865mJ | 352.788681mJ| 375.154930mJ| 2022.206927mJ| 773.380510mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 17.6483mm2  | 17.6483mm2 | 17.6483mm2 | 17.6483mm2  | 17.6483mm2  |
|**Subthreshold Leakage**| 2.52133W     | 2.52133W    | 2.52133W    | 2.52133W     | 2.52133W     |
|**Gate Leakage**     | 0.0190255W   | 0.0190255W  | 0.0190255W  | 0.0190255W   | 0.0190255W   |
|**Runtime Dynamic**  | 0.500792W    | 0.494643W   | 0.560601W   | 0.208611W    | 0.298971W    |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 12.8774mm2  | 12.8774mm2 | 12.8774mm2 | 12.8774mm2  | 12.8774mm2  |
|**Subthreshold Leakage**| 0.00887322W  | 0.00887322W | 0.00887322W | 0.00887322W  | 0.00887322W  |
|**Gate Leakage**     | 0.00107583W  | 0.00107583W | 0.00107583W | 0.00107583W  | 0.00107583W  |
|**Runtime Dynamic**  | 0.0054123W   | 0.000714191W| 2.96883e-05W| 0.0104919W   | 0.0079505W   |

Machine 10
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.53304      |  1.13387     |  1.18135     |  7.03865      |  2.62076      |
|**Energy**           | 432.092289mJ | 317.346593mJ| 339.501954mJ| 1781.298606mJ| 686.255441mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 24.8691mm2  | 24.8691mm2 | 24.8691mm2 | 24.8691mm2  | 24.8691mm2  |
|**Subthreshold Leakage**| 2.1569W      | 2.1569W     | 2.1569W     | 2.1569W      | 2.1569W      |
|**Gate Leakage**     | 0.0149794W   | 0.0149794W  | 0.0149794W  | 0.0149794W   | 0.0149794W   |
|**Runtime Dynamic**  | 0.562776W    | 0.550879W   | 0.627432W   | 0.234476W    | 0.334798W    |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 13.1659mm2  | 13.1659mm2 | 13.1659mm2 | 13.1659mm2  | 13.1659mm2  |
|**Subthreshold Leakage**| 0.0089513W   | 0.0089513W  | 0.0089513W  | 0.0089513W   | 0.0089513W   |
|**Gate Leakage**     | 0.0010833W   | 0.0010833W  | 0.0010833W  | 0.0010833W   | 0.0010833W   |
|**Runtime Dynamic**  | 0.00524748W  | 0.000706485W| 7.67215e-06W| 0.0106507W   | 0.00807119W  |

Machine 11
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.53330      |  1.13387     |  1.18134     |  7.03906      |  2.62076      |
|**Energy**           | 505.824863mJ | 370.237786mJ| 397.664856mJ| 2065.876826mJ| 798.598511mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 33.6123mm2  | 33.6123mm2 | 33.6123mm2 | 33.6123mm2  | 33.6123mm2  |
|**Subthreshold Leakage**| 2.51266W     | 2.51266W    | 2.51266W    | 2.51266W     | 2.51266W     |
|**Gate Leakage**     | 0.0177753W   | 0.0177753W  | 0.0177753W  | 0.0177753W   | 0.0177753W   |
|**Runtime Dynamic**  | 0.684361W    | 0.658608W   | 0.761073W   | 0.279748W    | 0.40463W     |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 13.3224mm2  | 13.3224mm2 | 13.3224mm2 | 13.3224mm2  | 13.3224mm2  |
|**Subthreshold Leakage**| 0.00910636W  | 0.00910636W | 0.00910636W | 0.00910636W  | 0.00910636W  |
|**Gate Leakage**     | 0.00110378W  | 0.00110378W | 0.00110378W | 0.00110378W  | 0.00110378W  |
|**Runtime Dynamic**  | 0.00527964W  | 0.000709866W| 4.11821e-06W| 0.0107879W   | 0.00817559W  |

Machine 12
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.52692      |  1.11289     |  1.17709     |  4.97248      |  1.98911      |
|**Energy**           | 759.740423mJ | 543.732892mJ| 599.778357mJ| 2186.578465mJ| 925.175516mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 47.5091mm2  | 47.5091mm2 | 47.5091mm2 | 47.5091mm2  | 47.5091mm2  |
|**Subthreshold Leakage**| 3.46055W     | 3.46055W    | 3.46055W    | 3.46055W     | 3.46055W     |
|**Gate Leakage**     | 0.0253457W   | 0.0253457W  | 0.0253457W  | 0.0253457W   | 0.0253457W   |
|**Runtime Dynamic**  | 1.39563W     | 1.32014W    | 1.53157W    | 0.781482W    | 1.05094W     |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 18.5988mm2  | 18.5988mm2 | 18.5988mm2 | 18.5988mm2  | 18.5988mm2  |
|**Subthreshold Leakage**| 0.0117038W   | 0.0117038W  | 0.0117038W  | 0.0117038W   | 0.0117038W   |
|**Gate Leakage**     | 0.00179366W  | 0.00179366W | 0.00179366W | 0.00179366W  | 0.00179366W  |
|**Runtime Dynamic**  | 0.0135256W   | 0.0013786W  | 1.24943e-05W| 0.0242844W   | 0.0171283W   |

Machine 13
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.51798      |  1.09894     |  1.17546     |  3.71467      |  1.65385      |
|**Energy**           | 803.770410mJ | 578.313878mJ| 627.521133mJ| 1937.308130mJ| 843.710064mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 37.0374mm2  | 37.0374mm2 | 37.0374mm2 | 37.0374mm2  | 37.0374mm2  |
|**Subthreshold Leakage**| 3.07114W     | 3.07114W    | 3.07114W    | 3.07114W     | 3.07114W     |
|**Gate Leakage**     | 0.0189889W   | 0.0189889W  | 0.0189889W  | 0.0189889W   | 0.0189889W   |
|**Runtime Dynamic**  | 2.02243W     | 2.05169W    | 2.13199W    | 1.93053W     | 1.84556W     |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 83.8533mm2  | 83.8533mm2 | 83.8533mm2 | 83.8533mm2  | 83.8533mm2  |
|**Subthreshold Leakage**| 0.0425755W   | 0.0425755W  | 0.0425755W  | 0.0425755W   | 0.0425755W   |
|**Gate Leakage**     | 0.00935023W  | 0.00935023W | 0.00935023W | 0.00935023W  | 0.00935023W  |
|**Runtime Dynamic**  | 0.0641756W   | 0.00414374W | 4.26859e-05W| 0.059716W    | 0.0378429W   |

Machine 14
-------------

| Benchmark           | 401bzip2      | 429mcf       | 456hmmer     | 458sjeng      | 470lbm        |
|---------------------|---------------|--------------|--------------|---------------|---------------|
|**CPI**              |  1.60383      |  1.10248     |  1.17723     |  3.71585      |  1.65512      |
|**Energy**           | 813.284810mJ | 538.886712mJ| 604.462870mJ| 1735.677251mJ| 802.837473mJ |
|**Core Data**        |               |              |              |               |               |
|**Area**             | 37.6015mm2  | 37.6015mm2 | 37.6015mm2 | 37.6015mm2  | 37.6015mm2  |
|**Subthreshold Leakage**| 2.91049W     | 2.91049W    | 2.91049W    | 2.91049W     | 2.91049W     |
|**Gate Leakage**     | 0.0186922W   | 0.0186922W  | 0.0186922W  | 0.0186922W   | 0.0186922W   |
|**Runtime Dynamic**  | 1.85762W     | 1.85455W    | 2.10352W    | 1.51223W     | 1.74124W     |
|**L2 Data**          |               |              |              |               |               |
|**Area**             | 41.0389mm2  | 41.0389mm2 | 41.0389mm2 | 41.0389mm2  | 41.0389mm2  |
|**Subthreshold Leakage**| 0.0246046W   | 0.0246046W  | 0.0246046W  | 0.0246046W   | 0.0246046W   |
|**Gate Leakage**     | 0.00569396W  | 0.00569396W | 0.00569396W | 0.00569396W  | 0.00569396W  |
|**Runtime Dynamic**  | 0.186285W    | 0.00910992W | 0.00722684W | 0.116216W    | 0.0737266W   |

Υπολογισμοί EDAP
----------------

|  Machine #1         |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 479.262916  | D = 0.153747 | A = 32.2026 | EDAP = 2372.8561662 |mm2mJs|
|Bench: 429mcf        | E = 353.673161  | D = 0.113881 | A = 32.2026 | EDAP = 1297.01295388|mm2mJs|
|Bench: 456hmmer      | E = 374.025984  | D = 0.118264 | A = 32.2026 | EDAP = 1424.44365679|mm2mJs|
|Bench: 458sjeng      | E = 2029.421792 | D = 0.705755 | A = 32.2026 | EDAP = 46122.9652873|mm2mJs|
|Bench: 470lbm        | E = 772.186533  | D = 0.262833 | A = 32.2026 | EDAP = 6535.71420337|mm2mJs|

|  Machine #2         |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 448.583068  | D = 0.159489 | A = 30.545  | EDAP = 2185.31346336|mm2mJs|
|Bench: 429mcf        | E = 319.200019  | D = 0.113756 | A = 30.545  | EDAP = 1109.1169708 |mm2mJs|
|Bench: 456hmmer      | E = 340.093648  | D = 0.11899  | A = 30.545  | EDAP = 1236.0872153 |mm2mJs|
|Bench: 458sjeng      | E = 1847.874082 | D = 0.705755 | A = 30.545  | EDAP = 39835.1509554|mm2mJs|
|Bench: 470lbm        | E = 702.117716  | D = 0.263117 | A = 30.545  | EDAP = 5642.85602578|mm2mJs|

|  Machine #3         |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 443.974563  | D = 0.153748 | A = 30.6957 | EDAP = 2095.29465528|mm2mJs|
|Bench: 429mcf        | E = 325.841879  | D = 0.113559 | A = 30.6957 | EDAP = 1135.81082288|mm2mJs|
|Bench: 456hmmer      | E = 346.879665  | D = 0.118264 | A = 30.6957 | EDAP = 1259.24126422|mm2mJs|
|Bench: 458sjeng      | E = 1867.427376 | D = 0.705757 | A = 30.6957 | EDAP = 40455.3960532|mm2mJs|
|Bench: 470lbm        | E = 714.836635  | D = 0.262833 | A = 30.6957 | EDAP = 5767.18968328|mm2mJs|

|  Machine #4         |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 484.395309  | D = 0.156092 | A = 26.7986 | EDAP = 2026.24837862|mm2mJs|
|Bench: 429mcf        | E = 351.834552  | D = 0.113766 | A = 26.7986 | EDAP = 1072.66246089|mm2mJs|
|Bench: 456hmmer      | E = 373.450192  | D = 0.118263 | A = 26.7986 | EDAP = 1183.56928204|mm2mJs|
|Bench: 458sjeng      | E = 2023.243595 | D = 0.705935 | A = 26.7986 | EDAP = 38275.8633321|mm2mJs|
|Bench: 470lbm        | E = 771.599882  | D = 0.263078 | A = 26.7986 | EDAP = 5439.87337335|mm2mJs|

|  Machine #5         |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 488.872194  | D = 0.157986 | A = 23.4957 | EDAP = 1814.68950703|mm2mJs|
|Bench: 429mcf        | E = 352.090438  | D = 0.11394  | A = 23.4957 | EDAP = 942.581331991|mm2mJs|
|Bench: 456hmmer      | E = 373.205506  | D = 0.118263 | A = 23.4957 | EDAP = 1037.01567824|mm2mJs|
|Bench: 458sjeng      | E = 2019.207734 | D = 0.706012 | A = 23.4957 | EDAP = 33495.1149163|mm2mJs|
|Bench: 470lbm        | E = 771.564619  | D = 0.263263 | A = 23.4957 | EDAP = 4772.55034787|mm2mJs|

|  Machine #6         |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 565.397385  | D = 0.152645 | A = 38.4487 | EDAP = 3318.31827678|mm2mJs|
|Bench: 429mcf        | E = 417.055032  | D = 0.113393 | A = 38.4487 | EDAP = 1818.28213336|mm2mJs|
|Bench: 456hmmer      | E = 444.17898   | D = 0.118217 | A = 38.4487 | EDAP = 2018.92226175|mm2mJs|
|Bench: 458sjeng      | E = 2391.223349 | D = 0.703833 | A = 38.4487 | EDAP = 64710.0042571|mm2mJs|
|Bench: 470lbm        | E = 912.449275  | D = 0.262713 | A = 38.4487 | EDAP = 9216.62578546|mm2mJs|

|  Machine #7         |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 330.17921   | D = 0.16382  | A = 30.9957 | EDAP = 1676.55611683|mm2mJs|
|Bench: 429mcf        | E = 234.703784  | D = 0.115267 | A = 30.9957 | EDAP = 838.545302696|mm2mJs|
|Bench: 456hmmer      | E = 244.071482  | D = 0.118598 | A = 30.9957 | EDAP = 897.213608814|mm2mJs|
|Bench: 458sjeng      | E = 2186.346204 | D = 0.166498 | A = 30.9957 | EDAP = 11283.1250827|mm2mJs|
|Bench: 470lbm        | E = 747.404782  | D = 0.391979 | A = 30.9957 | EDAP = 9080.71659234|mm2mJs|

|  Machine #8         |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 1004.26259  | D = 0.153312 | A = 56.0591 | EDAP = 8631.16770851|mm2mJs|
|Bench: 429mcf        | E = 720.447672  | D = 0.111498 | A = 56.0591 | EDAP = 4503.14198667|mm2mJs|
|Bench: 456hmmer      | E = 783.488522  | D = 0.117818 | A = 56.0591 | EDAP = 5174.76230326|mm2mJs|
|Bench: 458sjeng      | E = 3025.861934 | D = 0.501106 | A = 56.0591 | EDAP = 85001.1559411|mm2mJs|
|Bench: 470lbm        | E = 1244.418099 | D = 0.199148 | A = 56.0591 | EDAP = 13892.755394 |mm2mJs|

|  Machine #9         |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 479.634865  | D = 0.153478 | A = 32.2516 | EDAP = 2374.14992533|mm2mJs|
|Bench: 429mcf        | E = 352.788681  | D = 0.113403 | A = 32.2516 | EDAP = 1290.2992687 |mm2mJs|
|Bench: 456hmmer      | E = 375.15493   | D = 0.118144 | A = 32.2516 | EDAP = 1429.4652213 |mm2mJs|
|Bench: 458sjeng      | E = 2022.206927 | D = 0.70384  | A = 32.2516 | EDAP = 45904.0287791|mm2mJs|
|Bench: 470lbm        | E = 773.38051   | D = 0.262076 | A = 32.2516 | EDAP = 6536.89847003|mm2mJs|

|  Machine #10        |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 432.092289  | D = 0.153305 | A = 39.7609 | EDAP = 2633.83789432|mm2mJs|
|Bench: 429mcf        | E = 317.346593  | D = 0.113388 | A = 39.7609 | EDAP = 1430.72821353|mm2mJs|
|Bench: 456hmmer      | E = 339.501954  | D = 0.118136 | A = 39.7609 | EDAP = 1594.70643349|mm2mJs|
|Bench: 458sjeng      | E = 1781.298606 | D = 0.703865 | A = 39.7609 | EDAP = 49851.9676485|mm2mJs|
|Bench: 470lbm        | E = 686.255441  | D = 0.262076 | A = 39.7609 | EDAP = 7151.04084476|mm2mJs|

|  Machine #11        |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 505.824863  | D = 0.153331 | A = 48.6607 | EDAP = 3774.0573275 |mm2mJs|
|Bench: 429mcf        | E = 370.237786  | D = 0.113388 | A = 48.6607 | EDAP = 2042.80159073|mm2mJs|
|Bench: 456hmmer      | E = 397.664856  | D = 0.118135 | A = 48.6607 | EDAP = 2285.98906827|mm2mJs|
|Bench: 458sjeng      | E = 2065.876826 | D = 0.703906 | A = 48.6607 | EDAP = 70761.5672376|mm2mJs|
|Bench: 470lbm        | E = 798.598511  | D = 0.262076 | A = 48.6607 | EDAP = 10184.3683794|mm2mJs|

|  Machine #12        |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 759.740423  | D = 0.152692 | A = 67.8338 | EDAP = 7869.14711296|mm2mJs|
|Bench: 429mcf        | E = 543.732892  | D = 0.11129  | A = 67.8338 | EDAP = 4104.76118147|mm2mJs|
|Bench: 456hmmer      | E = 599.778357  | D = 0.11771  | A = 67.8338 | EDAP = 4789.06020226|mm2mJs|
|Bench: 458sjeng      | E = 2186.578465 | D = 0.497248 | A = 67.8338 | EDAP = 73753.7756944|mm2mJs|
|Bench: 470lbm        | E = 925.175516  | D = 0.198912 | A = 67.8338 | EDAP = 12483.3532935|mm2mJs|

|  Machine #13        |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 803.77041   | D = 0.151798 | A = 122.617 | EDAP = 14960.5909921|mm2mJs|
|Bench: 429mcf        | E = 578.313878  | D = 0.109894 | A = 122.617 | EDAP = 7792.70582771|mm2mJs|
|Bench: 456hmmer      | E = 627.521133  | D = 0.117547 | A = 122.617 | EDAP = 9044.62555856|mm2mJs|
|Bench: 458sjeng      | E = 1937.30813  | D = 0.371467 | A = 122.617 | EDAP = 88240.8383796|mm2mJs|
|Bench: 470lbm        | E = 843.710064  | D = 0.165386 | A = 122.617 | EDAP = 17109.7104254|mm2mJs|

|  Machine #14        |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 813.28481   | D = 0.160384 | A = 80.3662 | EDAP = 10482.7960257|mm2mJs|
|Bench: 429mcf        | E = 538.886712  | D = 0.110248 | A = 80.3662 | EDAP = 4774.6509529 |mm2mJs|
|Bench: 456hmmer      | E = 604.46287   | D = 0.117723 | A = 80.3662 | EDAP = 5718.79308821|mm2mJs|
|Bench: 458sjeng      | E = 1735.677251 | D = 0.371585 | A = 80.3662 | EDAP = 51832.3117924|mm2mJs|
|Bench: 470lbm        | E = 802.837473  | D = 0.165512 | A = 80.3662 | EDAP = 10678.9992427|mm2mJs|

|  Machine #idealNew  |                 |              |             |                     |      |
|---------------------|-----------------|--------------|-------------|---------------------|------|
|Bench: 401bzip2      | E = 254.217529  | D = 0.171643 | A = 14.4371 | EDAP = 629.957940215|mm2mJs|
|Bench: 429mcf        | E = 173.836834  | D = 0.115111 | A = 14.4371 | EDAP = 288.894048629|mm2mJs|
|Bench: 456hmmer      | E = 181.024929  | D = 0.118795 | A = 14.4371 | EDAP = 310.467762918|mm2mJs|
|Bench: 458sjeng      | E = 1615.123752 | D = 0.165906 | A = 14.4371 | EDAP = 3868.54685383|mm2mJs|
|Bench: 470lbm        | E = 554.728596  | D = 0.392222 | A = 14.4371 | EDAP = 3141.17743285|mm2mJs|


Γραφήματα με τις Συγκρίσεις Τιμών των Παραμέτρων
------------------------------------------------
#### Συσχέτιση Μνημών
<img src="Part2/charts/GraphAssociativity.png"/>
<img src="Part2/charts/GraphAssociativityImprovement.png"/>

Παρατηρούμε ότι 2-way είναι η μεγαλύτερη τιμή που μπορούμε να δώσουμε χωρίς να καταχρώμαστε το εμβαδό σιλικόνης που θα απαιτηθεί. Επιλέγουμε 2-way Associativity ώς ιδανική λύση.

#### Μέγεθος Γραμμής Κρυφών Μνημών
<img src="Part2/charts/GraphCacheLine.png"/>
<img src="Part2/charts/GraphCacheLineImprovement.png"/>

Παρατηρούμε ότι επεξεργαστές με μεγαλύτερη γραμμή μνημών απαιτούν πολύ μεγαλύτερο εμβαδό αλλά και ισχύ. Θεωρούμε ιδανική τιμή το 32 για την Γραμμή των Κρυφών Μνημών.

#### Μέγεθος L1 Κρυφής Μνήμης Δεδομένων
<img src="Part2/charts/GraphL1dSize.png"/>
<img src="Part2/charts/GraphL1dSizeImprovement.png"/>

Παρατηρούμε ότι μεγαλύτερα μεγέθη της Κρυφής Μνήμης Πρώτου επιπέδου προκαλούν αύξηση τόσο στην κατανάλωση ισχύος όσο και στο εμβαδό που θα καταλαμβάνει ο επεξεργαστής. Λόγο των μηδαμινών βελτιώσεων επιλέγουμε τα 128kB ως ιδανική τιμή.

#### Μέγεθος L2 Κρυφής Μνήμης
<img src="Part2/charts/GraphL2Size.png"/>
<img src="Part2/charts/GraphL2SizeImprovement.png"/>

Παρατηρούμε ότι μεγαλύτερα μεγέθη της Κρυφής Μνήμης Δεύτερου επιπέδου προκαλούν αύξηση τόσο στην κατανάλωση ισχύος όσο και στο εμβαδό που θα καταλαμβάνει ο επεξεργαστής. Ταυτόχρωνα επιφέρουν μικρή βελτίωση επιδώσεων στα περισσότερα benchmark. Λόγο των μηδαμινών βελτιώσεων επιλέγουμε τα 1024kB ως ιδανική τιμή.

### 3.

Από τα αποτελέσματα που πήραμε από το McPat αποκτήσαμε μία πιο έγκυρη εικόνα του κόστους σε σχέση με τις τιμές των διαφόρων παραμέτρων του συστήματος κρυφών μνημών του επεξεργαστή. Έχοντας και τα αποτελέσματα των επιδόσεων των διαφόρων συνδυασμών καταφέραμε να επιλέξουμε τις καταλληλότερες τιμές.
Συγκρίνοντας τις καινούριες επιλογές με αυτές που είχαμε αποφασήσει στο τέλος της δεύτερης άσκησης και βάση της Συνάρτησης κόστους που φτιάξαμε, παρατηρούμε ότι μερικές από τις επιλογές μας δεν ήταν ιδανικές. Πιο συγκεκριμένα, με την συνάρτηση κόστους μας δεν υπολογίζαμε την επίδραση του μεγέθους γραμμής των μνημών. Επίσης υπερεκτιμούσαμε το κόστος μεγέθους των κρυφών μνημών σε εμβαδό. Τέλος δεν είχαμε καμία εκτίμηση κόστους σε ισχύ και έτσι αγνοήσαμε τελείως την τεράστια απαίτηση που είχε το μέγεθος γραμμής σε αυτό.
