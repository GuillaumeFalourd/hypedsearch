import unit_tests
import unittest
import os
from src.postprocessing import summary

class test_postprocessing(unittest.TestCase):
    def setUp(self) -> None:
        global output_dir, results
        output_dir = os.path.join("unit_tests")
        results = {'NOD2_E3.21510.21510.2.pkl': Alignments(spectrum=Spectrum(spectrum=[86.09624481201172, 87.09951782226562, 101.0701675415039, 132.1012420654297, 185.1271209716797, 199.18028259277344, 201.12388610839844, 212.10206604003906, 215.1410369873047, 227.17416381835938, 229.11610412597656, 245.1857452392578, 286.1751708984375, 357.1766662597656, 399.26287841796875, 425.2383728027344, 440.212646484375, 458.2256164550781, 527.32275390625, 553.2962646484375, 571.3082275390625, 624.3322143554688, 642.3450927734375, 737.4176635742188, 755.427734375], abundance=[27327.09765625, 1976.5467529296875, 1414.1640625, 8025.5380859375, 612.0140991210938, 855.3250122070312, 4002.779052734375, 572.3911743164062, 606.1412963867188, 670.3060302734375, 827.6177978515625, 2575.84619140625, 934.2576904296875, 1107.2940673828125, 546.85595703125, 540.0253295898438, 928.4806518554688, 760.0152587890625, 523.9761962890625, 1501.77880859375, 572.0018310546875, 1440.9600830078125, 3004.942138671875, 647.4628295898438, 1706.5208740234375], total_intensity=63680.338928222656, ms_level=2, scan_number=4, precursor_mass=500.30807, precursor_charge=2, file_name='/mnt/c/Users/Maxim/Documents/Layer_Lab/Database/Hybrid_inputs/hybrid_nod2e3.mzML', id='NOD2_E3.21510.21510.2.pkl', other_metadata={}), alignments=[SequenceAlignment(proteins=[], sequence='DLQTLALLL', b_score=6, y_score=2, total_score=8, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148399336), SequenceAlignment(proteins=[], sequence='DLQTLAILL', b_score=6, y_score=2, total_score=8, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148399336), SequenceAlignment(proteins=[], sequence='DLQTLALII', b_score=6, y_score=2, total_score=8, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148399336), SequenceAlignment(proteins=[], sequence='DLQTLALIL', b_score=6, y_score=2, total_score=8, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148399336), SequenceAlignment(proteins=[], sequence='DLQTLAIIL', b_score=6, y_score=2, total_score=8, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148399336), SequenceAlignment(proteins=[], sequence='DLQTLALLI', b_score=6, y_score=2, total_score=8, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148399336), SequenceAlignment(proteins=[], sequence='DLQTLAILI', b_score=6, y_score=2, total_score=8, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148399336), SequenceAlignment(proteins=[], sequence='LTALGADILL', b_score=6, y_score=2, total_score=8, precursor_distance=0.00019424999993589154, total_mass_error=0.0132002299608871), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='TIALQDIIL', hybrid_sequence='TIALQ-DIIL', b_score=6, y_score=2, total_score=7.5, precursor_distance=0.00019424999993589154, total_mass_error=0.0132002299608871), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='TIALQDILL', hybrid_sequence='TIALQ-DILL', b_score=6, y_score=2, total_score=7.5, precursor_distance=0.00019424999993589154, total_mass_error=0.0132002299608871), SequenceAlignment(proteins=[], sequence='NELTLAILI', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019474999993462916, total_mass_error=0.0052057781249743584), SequenceAlignment(proteins=[], sequence='NELTLALIL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019474999993462916, total_mass_error=0.0052057781249743584), SequenceAlignment(proteins=[], sequence='NELTLAIIL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019474999993462916, total_mass_error=0.0052057781249743584), SequenceAlignment(proteins=[], sequence='NELTLAILL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019474999993462916, total_mass_error=0.0052057781249743584), SequenceAlignment(proteins=[], sequence='VTEQLAILL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.005530276289050562), SequenceAlignment(proteins=[], sequence='VTEQLALIL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.005530276289050562), SequenceAlignment(proteins=[], sequence='EVQITAILI', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.006312067070354033), SequenceAlignment(proteins=[], sequence='EVQITALIL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.006312067070354033), SequenceAlignment(proteins=[], sequence='EVQITAIIL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.006312067070354033), SequenceAlignment(proteins=[], sequence='EVQITAILL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.006312067070354033), SequenceAlignment(proteins=[], sequence='DLQTLIALL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.006762425585918663), SequenceAlignment(proteins=[], sequence='DLQTLLALL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.006762425585918663), SequenceAlignment(proteins=[], sequence='LATALTSPII', b_score=4, y_score=3, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.007249227500011557), SequenceAlignment(proteins=[], sequence='LATALTSPLI', b_score=4, y_score=3, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.007249227500011557), SequenceAlignment(proteins=[], sequence='LATALTSPLL', b_score=4, y_score=3, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.007249227500011557), SequenceAlignment(proteins=[], sequence='LATALTSPIL', b_score=4, y_score=3, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.007249227500011557), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DLQTLAIII', hybrid_sequence='DLQTLA-III', b_score=6, y_score=2, total_score=7.0, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148399336), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DLGATLALIL', hybrid_sequence='DLGAT-LALIL', b_score=6, y_score=2, total_score=7.0, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148399336), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LDQTLAILL', hybrid_sequence='LDQT-LAILL', b_score=6, y_score=2, total_score=7.0, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148399336), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LDQTLALIL', hybrid_sequence='LDQT-LALIL', b_score=6, y_score=2, total_score=7.0, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148399336), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DLGATLAILL', hybrid_sequence='DLGAT-LAILL', b_score=6, y_score=2, total_score=7.0, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148399336), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='VEQTLALIL', hybrid_sequence='VEQT-LALIL', b_score=6, y_score=2, total_score=7.0, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148427758), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='VEQTLAILL', hybrid_sequence='VEQT-LAILL', b_score=6, y_score=2, total_score=7.0, precursor_distance=0.00019424999993589154, total_mass_error=0.007388087148427758), SequenceAlignment(proteins=[], sequence='ALTITTGPLL', b_score=4, y_score=3, total_score=7, precursor_distance=0.0001937499998803105, total_mass_error=0.007913308164205546), SequenceAlignment(proteins=[], sequence='ALTLDQILL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.008537669726507602), SequenceAlignment(proteins=[], sequence='IATLDQILL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.008537669726507602), SequenceAlignment(proteins=[], sequence='AITLDQILL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.008537669726507602), SequenceAlignment(proteins=[], sequence='LATLDQILL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.008537669726507602), SequenceAlignment(proteins=[], sequence='LTALDQILL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.00922175871090758), SequenceAlignment(proteins=[], sequence='TIALDQILL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.00922175871090758), SequenceAlignment(proteins=[], sequence='TLALDQILL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.00922175871090758), SequenceAlignment(proteins=[], sequence='ITALDQILL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.00922175871090758), SequenceAlignment(proteins=[], sequence='AITLQEVLI', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.01189047941400645), SequenceAlignment(proteins=[], sequence='AITLQLDLI', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.01189047941400645), SequenceAlignment(proteins=[], sequence='AITLQVEII', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.01189047941400645), SequenceAlignment(proteins=[], sequence='AITLQLDLL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.01189047941400645), SequenceAlignment(proteins=[], sequence='AITLQLDIL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.01189047941400645), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='AITLQDILL', hybrid_sequence='AITLQ-DILL', b_score=6, y_score=2, total_score=7.0, precursor_distance=0.00019424999993589154, total_mass_error=0.012516140976487122), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='AITLQDIIL', hybrid_sequence='AITLQ-DIIL', b_score=6, y_score=2, total_score=7.0, precursor_distance=0.00019424999993589154, total_mass_error=0.012516140976487122), SequenceAlignment(proteins=[], sequence='TIALQLDIL', b_score=5, y_score=2, total_score=7, precursor_distance=0.00019424999993589154, total_mass_error=0.012574568398406427)]), 'NOD2_E3.12771.12902.3.pkl': Alignments(spectrum=Spectrum(spectrum=[70.06509399414062, 101.0711898803711, 155.0814971923828, 212.10289001464844, 226.11825561523438, 301.151123046875, 341.1452331542969, 358.1719665527344, 440.2135009765625, 472.2144470214844, 511.2510986328125, 585.2991943359375, 639.3088989257812, 660.3319091796875, 660.8334350585938, 695.8516845703125, 752.392578125, 881.4356079101562, 994.5189819335938, 995.5225830078125, 1108.5623779296875, 1165.5831298828125, 1166.585205078125, 1465.7266845703125, 1466.729248046875], abundance=[27281.93359375, 9418.7080078125, 13158.416015625, 9428.8037109375, 12447.669921875, 47830.76953125, 8432.2744140625, 13165.791015625, 16802.490234375, 19610.171875, 14106.8603515625, 12565.205078125, 15957.138671875, 14542.2265625, 9493.626953125, 10875.111328125, 19026.494140625, 21746.3125, 22115.86328125, 8179.0341796875, 10758.201171875, 24602.515625, 9873.78125, 36875.671875, 20462.125], total_intensity=428757.1962890625, ms_level=2, scan_number=5, precursor_mass=977.48943, precursor_charge=3, file_name='/mnt/c/Users/Maxim/Documents/Layer_Lab/Database/Hybrid_inputs/hybrid_nod2e3.mzML', id='NOD2_E3.12771.12902.3.pkl', other_metadata={}), alignments=[HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DPQVAQLELGITADDEPLGRVSFELFA', hybrid_sequence='DPQVAQLELG-ITADDEPLGRVSFELFA', b_score=7, y_score=1, total_score=7.5, precursor_distance=0.008153300000003583, total_mass_error=0.020908997109643224), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='TQAGVEELDTTGVEQSLSGLSISSAPPAVS', hybrid_sequence='TQAGVEELD-TTGVEQSLSGLSISSAPPAVS', b_score=5, y_score=3, total_score=6.5, precursor_distance=0.0020176999996692757, total_mass_error=0.03282400109378614), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='NPEVFQPGELKDWFVGRSNAQGIDLN', hybrid_sequence='NPEVF-QPGELKDWFVGRSNAQGIDLN', b_score=4, y_score=3, total_score=6.0, precursor_distance=0.0035300333331633738, total_mass_error=0.014147186445597981), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='NPPYDKPGELKDWFVGRSNAQGIDLN', hybrid_sequence='NPPYDK-PGELKDWFVGRSNAQGIDLN', b_score=4, y_score=3, total_score=5.5, precursor_distance=0.0035330333332694863, total_mass_error=0.01795760343765096), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='NPPYDKGKKEEAGEKKKAVASEEETPA', hybrid_sequence='NPPYDKG-KKEEAGEKKKAVASEEETPA', b_score=4, y_score=2, total_score=5.0, precursor_distance=0.00680896666699482, total_mass_error=0.032376528749807676), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DPQVADATYETKESKKEDLVFIFWA', hybrid_sequence='DPQVA-DATYETKESKKEDLVFIFWA', b_score=3, y_score=2, total_score=4.5, precursor_distance=0.002637366666476737, total_mass_error=0.0030349926171879815), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='GADPVADATYETKESKKEDLVFIFWA', hybrid_sequence='GADPVA-DATYETKESKKEDLVFIFWA', b_score=3, y_score=2, total_score=4.5, precursor_distance=0.002637366666476737, total_mass_error=0.0030349926171879815), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='TGAAGRNSPGELKDWFVGRSNAQGIDLN', hybrid_sequence='TGAAGRNS-PGELKDWFVGRSNAQGIDLN', b_score=3, y_score=3, total_score=4.5, precursor_distance=0.0011263666665399796, total_mass_error=0.012394568203092149), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='TQAGVEEPGELKDWFVGRSNAQGIDLN', hybrid_sequence='TQAGVEE-PGELKDWFVGRSNAQGIDLN', b_score=3, y_score=3, total_score=4.5, precursor_distance=0.008615033333171596, total_mass_error=0.02468987429705294), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='PGGLGEDATYETKESKKEDLVFIFWA', hybrid_sequence='PGGLGE-DATYETKESKKEDLVFIFWA', b_score=3, y_score=2, total_score=4.0, precursor_distance=0.002637366666476737, total_mass_error=0.0002286460938023538), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='NPDLADATYETKESKKEDLVFIFWA', hybrid_sequence='NPDLA-DATYETKESKKEDLVFIFWA', b_score=3, y_score=2, total_score=4.0, precursor_distance=0.0026376999999229156, total_mass_error=0.000695361913983561), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='PGAGDLDATYETKESKKEDLVFIFWA', hybrid_sequence='PGAGDL-DATYETKESKKEDLVFIFWA', b_score=3, y_score=2, total_score=4.0, precursor_distance=0.0026373666667041107, total_mass_error=0.0026023158593773132), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='GKDGNNGLIANFTITSLQHWEFAPNSV', hybrid_sequence='GKDGNN-GLIANFTITSLQHWEFAPNSV', b_score=3, y_score=1, total_score=4, precursor_distance=0.0035300333332770606, total_mass_error=0.0026836929689011413), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='GPVEGADATYETKESKKEDLVFIFWA', hybrid_sequence='GPVEGA-DATYETKESKKEDLVFIFWA', b_score=3, y_score=2, total_score=4.0, precursor_distance=0.0026373666667041107, total_mass_error=0.0027139545312593327), SequenceAlignment(proteins=[], sequence='PGGEPGAHSALDTREEKRLLDEGHYPV', b_score=3, y_score=1, total_score=4, precursor_distance=0.004873366666743095, total_mass_error=0.0039017289841183356), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='GPGEPGAHSALDTREEKRLLDEGHYPV', hybrid_sequence='GPG-EPGAHSALDTREEKRLLDEGHYPV', b_score=3, y_score=1, total_score=4, precursor_distance=0.004873366666743095, total_mass_error=0.0039017289841183356), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='PGADPGAHSALDTREEKRLLDEGHYPV', hybrid_sequence='PGAD-PGAHSALDTREEKRLLDEGHYPV', b_score=3, y_score=1, total_score=4, precursor_distance=0.004873366666743095, total_mass_error=0.00418612839817456), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='GPADPGAHSALDTREEKRLLDEGHYPV', hybrid_sequence='GPAD-PGAHSALDTREEKRLLDEGHYPV', b_score=3, y_score=1, total_score=4, precursor_distance=0.004873366666743095, total_mass_error=0.00418612839817456), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='GADPVAGPEQLELGGGPGAGDLQTLALEVAQ', hybrid_sequence='GADPVAGPE-QLELGGGPGAGDLQTLALEVAQ', b_score=3, y_score=1, total_score=4, precursor_distance=0.006813300000089839, total_mass_error=0.014854151640236068), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='GADPVAGPEAGLELGGGPGAGDLQTLALEVAQ', hybrid_sequence='GADPVAGPEAG-LELGGGPGAGDLQTLALEVAQ', b_score=3, y_score=1, total_score=4, precursor_distance=0.006813300000089839, total_mass_error=0.014854151640463442), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='PGAGDLQTLQAVMEMMSQKIQQLTALGA', hybrid_sequence='PGAGDLQTL-QAVMEMMSQKIQQLTALGA', b_score=4, y_score=1, total_score=4.0, precursor_distance=0.008226633333606514, total_mass_error=0.017309984101785858), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='AAGTGVSGAAPSWEFAPNSVHYLLTLWQ', hybrid_sequence='AAGTGVSGAAPS-WEFAPNSVHYLLTLWQ', b_score=3, y_score=2, total_score=3.5, precursor_distance=0.0021913666664659104, total_mass_error=0.0018756110160893513), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='AAAPEADATYETKESKKEDLVFIFWA', hybrid_sequence='AAAPEA-DATYETKESKKEDLVFIFWA', b_score=2, y_score=2, total_score=3.5, precursor_distance=0.0026373666667041107, total_mass_error=0.00270671191361771), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='SAPSPADATYETKESKKEDLVFIFWA', hybrid_sequence='SAPSPA-DATYETKESKKEDLVFIFWA', b_score=2, y_score=2, total_score=3.5, precursor_distance=0.0026376999999229156, total_mass_error=0.002707211913843821), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='PGGEEVLREQAGGDARIEEFKSINTEV', hybrid_sequence='PGGEEVLREQAGGDA-RIEEFKSINTEV', b_score=4, y_score=1, total_score=3.5, precursor_distance=0.0015720333334456882, total_mass_error=0.0070548014843723195), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LYYADATYETKESKKEDLVFIFWA', hybrid_sequence='LYYA-DATYETKESKKEDLVFIFWA', b_score=2, y_score=2, total_score=3.5, precursor_distance=0.0013023666665503697, total_mass_error=0.012433245664283277), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='PGADPVYFKEEKYKDAIHFYNKSLA', hybrid_sequence='PGADPV-YFKEEKYKDAIHFYNKSLA', b_score=3, y_score=1, total_score=3.5, precursor_distance=0.006186300000194933, total_mass_error=0.013800057773465824), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='PGDAPGAHSALDTREEKRLLDEGHYPV', hybrid_sequence='PGDA-PGAHSALDTREEKRLLDEGHYPV', b_score=2, y_score=1, total_score=3, precursor_distance=0.004873366666743095, total_mass_error=0.0038233086325476506), SequenceAlignment(proteins=[], sequence='NPEPGAHSALDTREEKRLLDEGHYPV', b_score=2, y_score=1, total_score=3, precursor_distance=0.004873700000075587, total_mass_error=0.003892986366849982), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='PNEPGAHSALDTREEKRLLDEGHYPV', hybrid_sequence='PN-EPGAHSALDTREEKRLLDEGHYPV', b_score=2, y_score=1, total_score=3, precursor_distance=0.004873700000075587, total_mass_error=0.003892986366849982), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='QPDPGAHSALDTREEKRLLDEGHYPV', hybrid_sequence='QPD-PGAHSALDTREEKRLLDEGHYPV', b_score=2, y_score=1, total_score=3, precursor_distance=0.004873366666743095, total_mass_error=0.0041788857809876845), SequenceAlignment(proteins=['COF1_MOUSE'], sequence='YALYDATYETKESKKEDLVFIFWA', b_score=1, y_score=2, total_score=3, precursor_distance=0.0013023666665503697, total_mass_error=0.007953787226938402), SequenceAlignment(proteins=['COF1_MOUSE'], sequence='YALYDATYETKESKKEDLVFIFWA', b_score=1, y_score=2, total_score=3, precursor_distance=0.0013023666665503697, total_mass_error=0.007953787226938402), SequenceAlignment(proteins=[], sequence='YLYVLANLCEAPYPIDRIEMAMDKV', b_score=1, y_score=2, total_score=3, precursor_distance=0.0012300333332859736, total_mass_error=0.009169899531684678), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='TGAAGRNEVNFQEYVAFLGALALIYNE', hybrid_sequence='TGAAGRN-EVNFQEYVAFLGALALIYNE', b_score=2, y_score=1, total_score=3, precursor_distance=0.004848633333608632, total_mass_error=0.01171570882826245), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='AAGTGVSVMENGKVIEFDKPEVLAEKPD', hybrid_sequence='AAGTGVS-VMENGKVIEFDKPEVLAEKPD', b_score=2, y_score=1, total_score=3, precursor_distance=0.00927663333345663, total_mass_error=0.01835770882809129), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='GDPGLGVRPPRDYPGTMAGRFGSRDALD', hybrid_sequence='GDPGLGVR-PPRDYPGTMAGRFGSRDALD', b_score=2, y_score=1, total_score=3, precursor_distance=0.007048033333376225, total_mass_error=0.019610553750396775), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='PNPVDAMKQAVMEMMSQKIQQLTALGA', hybrid_sequence='PNPVD-AMKQAVMEMMSQKIQQLTALGA', b_score=2, y_score=1, total_score=2.5, precursor_distance=0.0023066333337737888, total_mass_error=0.007366377656353507), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DPQPGAHSALDTREEKRLLDEGHYPV', hybrid_sequence='DPQ-PGAHSALDTREEKRLLDEGHYPV', b_score=1, y_score=1, total_score=2, precursor_distance=0.004873366666743095, total_mass_error=0.003816066015360775), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='GPGPGSNFRGWEFAPNSVHYLLTLWQ', hybrid_sequence='GPGPGSNFRG-WEFAPNSVHYLLTLWQ', b_score=3, y_score=1, total_score=2.0, precursor_distance=0.005490366666435875, total_mass_error=0.004498948281224102), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='PVDLLQFYFPESFDRLPRDSGLFDG', hybrid_sequence='P-VDLLQFYFPESFDRLPRDSGLFDG', b_score=0, y_score=1, total_score=1, precursor_distance=0.005936366666787762, total_mass_error=0.005082285312482782), SequenceAlignment(proteins=['HPS3_MOUSE'], sequence='FLEPLSEDTVAGLSTHALCHTRLQEY', b_score=0, y_score=1, total_score=1, precursor_distance=0.006153033333248459, total_mass_error=0.00540728531223067), SequenceAlignment(proteins=['HPS3_MOUSE'], sequence='FLEPLSEDTVAGLSTHALCHTRLQEY', b_score=0, y_score=1, total_score=1, precursor_distance=0.006153033333248459, total_mass_error=0.00540728531223067), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='AANKDQEVNFQEYVAFLGALALIYNE', hybrid_sequence='AA-NKDQEVNFQEYVAFLGALALIYNE', b_score=0, y_score=1, total_score=1, precursor_distance=0.001103966666960332, total_mass_error=0.005478214687855143), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='PTRGQDVGRYQVSWSLEHKSAHAGTY', hybrid_sequence='P-TRGQDVGRYQVSWSLEHKSAHAGTY', b_score=0, y_score=1, total_score=1, precursor_distance=0.008174699999813129, total_mass_error=0.008439785312702952), SequenceAlignment(proteins=['PPIA_MOUSE'], sequence='MVNPTVFFDITADDEPLGRVSFELFA', b_score=0, y_score=1, total_score=1, precursor_distance=0.008554033333325606, total_mass_error=0.009008785312971668), SequenceAlignment(proteins=['PPIA_MOUSE'], sequence='MVNPTVFFDITADDEPLGRVSFELFA', b_score=0, y_score=1, total_score=1, precursor_distance=0.008554033333325606, total_mass_error=0.009008785312971668), SequenceAlignment(proteins=['PFD5_MOUSE'], sequence='QEKHAMKQAVMEMMSQKIQQLTALGA', b_score=0, y_score=1, total_score=1, precursor_distance=0.0060513000004220885, total_mass_error=0.012899214687877247), SequenceAlignment(proteins=['PFD5_MOUSE'], sequence='QEKHAMKQAVMEMMSQKIQQLTALGA', b_score=0, y_score=1, total_score=1, precursor_distance=0.0060513000004220885, total_mass_error=0.012899214687877247), SequenceAlignment(proteins=['CELR3_MOUSE'], sequence='TLPRRQPPRDYPGTMAGRFGSRDALD', b_score=0, y_score=1, total_score=1, precursor_distance=0.00882496666656607, total_mass_error=0.017059714687320593)]), 'NOD2_E3.7065.7065.2.pkl': Alignments(spectrum=Spectrum(spectrum=[70.06450653076172, 71.06840515136719, 86.09596252441406, 110.06985473632812, 129.10279846191406, 159.04664611816406, 169.13323974609375, 187.0726776123047, 197.128173828125, 199.1802520751953, 201.1237335205078, 202.12591552734375, 204.1324920654297, 229.11782836914062, 301.1584777832031, 326.1693420410156, 457.222412109375, 465.7381896972656, 466.2387390136719, 466.7373352050781, 533.2760009765625, 734.3452758789062, 735.3536987304688, 930.4730224609375, 931.4747314453125], abundance=[2425.837890625, 322.0297546386719, 999.3156127929688, 328.1689758300781, 1740.923828125, 418.3720703125, 1137.051513671875, 318.41552734375, 601.9422607421875, 418.1022644042969, 2938.79052734375, 539.1080322265625, 509.41046142578125, 992.1661987304688, 495.8224792480469, 341.8166809082031, 334.64013671875, 4750.68505859375, 1969.203369140625, 615.723388671875, 483.45587158203125, 935.2410278320312, 392.87188720703125, 734.689453125, 582.3766479492188], total_intensity=25326.160919189453, ms_level=2, scan_number=6, precursor_mass=579.795258, precursor_charge=2, file_name='/mnt/c/Users/Maxim/Documents/Layer_Lab/Database/Hybrid_inputs/hybrid_nod2e3.mzML', id='NOD2_E3.7065.7065.2.pkl', other_metadata={}), alignments=[SequenceAlignment(proteins=[], sequence='LDDLPGSEVLT', b_score=3, y_score=2, total_score=5, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), SequenceAlignment(proteins=[], sequence='DLDLPGSEVLT', b_score=3, y_score=2, total_score=5, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), SequenceAlignment(proteins=[], sequence='IDDLPGSEVLT', b_score=3, y_score=2, total_score=5, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), SequenceAlignment(proteins=[], sequence='DIDLPGSEVLT', b_score=3, y_score=2, total_score=5, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), SequenceAlignment(proteins=[], sequence='VEDLPGSEVLT', b_score=3, y_score=2, total_score=5, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281367668), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LDDIPGSEVLT', hybrid_sequence='LDDI-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DIVEPGSEVLT', hybrid_sequence='DIVE-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='IDEVPGSEVLT', hybrid_sequence='IDEV-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DIIDPGSEVLT', hybrid_sequence='DIID-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LDVEPGSEVLT', hybrid_sequence='LDVE-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DILDPGSEVLT', hybrid_sequence='DILD-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LDEVPGSEVLT', hybrid_sequence='LDEV-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LDIDPGSEVLT', hybrid_sequence='LDID-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='IDDIPGSEVLT', hybrid_sequence='IDDI-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DLIDPGSEVLT', hybrid_sequence='DLID-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DLDIPGSEVLT', hybrid_sequence='DLDI-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='IDLDPGSEVLT', hybrid_sequence='IDLD-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DIDIPGSEVLT', hybrid_sequence='DIDI-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LDLDPGSEVLT', hybrid_sequence='LDLD-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DLVEPGSEVLT', hybrid_sequence='DLVE-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DLEVPGSEVLT', hybrid_sequence='DLEV-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281282403), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='EVEVPGSEVLT', hybrid_sequence='EVEV-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281367668), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='VEEVPGSEVLT', hybrid_sequence='VEEV-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281367668), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='VEVEPGSEVLT', hybrid_sequence='VEVE-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281367668), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='VELDPGSEVLT', hybrid_sequence='VELD-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281367668), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='VEDIPGSEVLT', hybrid_sequence='VEDI-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281367668), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='EVDIPGSEVLT', hybrid_sequence='EVDI-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281367668), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='EVDLPGSEVLT', hybrid_sequence='EVD-LPGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281367668), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='EVLDPGSEVLT', hybrid_sequence='EVLD-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281367668), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='EVVEPGSEVLT', hybrid_sequence='EVVE-PGSEVLT', b_score=3, y_score=2, total_score=4, precursor_distance=0.002810749999980544, total_mass_error=0.016540653281367668), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LDDLPGACGGKL', hybrid_sequence='LDDLPGA-CGGKL', b_score=3, y_score=2, total_score=3.5, precursor_distance=0.00045124999996914994, total_mass_error=0.010139305156229739), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='IDMQKDPQAL', hybrid_sequence='ID-MQKDPQAL', b_score=1, y_score=2, total_score=3, precursor_distance=0.00045124999996914994, total_mass_error=0.003260979531233943), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DIMQKDPQAL', hybrid_sequence='DI-MQKDPQAL', b_score=1, y_score=2, total_score=3, precursor_distance=0.00045124999996914994, total_mass_error=0.003260979531233943), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LDMQKDPQAL', hybrid_sequence='LD-MQKDPQAL', b_score=1, y_score=2, total_score=3, precursor_distance=0.00045124999996914994, total_mass_error=0.003260979531233943), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DLMQKDPQAL', hybrid_sequence='DL-MQKDPQAL', b_score=1, y_score=2, total_score=3, precursor_distance=0.00045124999996914994, total_mass_error=0.003260979531233943), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='EVMQKDPQAL', hybrid_sequence='EV-MQKDPQAL', b_score=1, y_score=2, total_score=3, precursor_distance=0.00045124999996914994, total_mass_error=0.0032609795312623646), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='VEMQKDPQAL', hybrid_sequence='VE-MQKDPQAL', b_score=1, y_score=2, total_score=3, precursor_distance=0.00045124999996914994, total_mass_error=0.0032609795312623646), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LDMRPLDAVE', hybrid_sequence='LD-MRPLDAVE', b_score=1, y_score=2, total_score=3, precursor_distance=0.00045174999991104414, total_mass_error=0.003261479531289524), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='IDMRPLDAVE', hybrid_sequence='ID-MRPLDAVE', b_score=1, y_score=2, total_score=3, precursor_distance=0.00045174999991104414, total_mass_error=0.003261479531289524), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DIMRPLDAVE', hybrid_sequence='DI-MRPLDAVE', b_score=1, y_score=2, total_score=3, precursor_distance=0.00045174999991104414, total_mass_error=0.003261479531289524), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DLMRPLDAVE', hybrid_sequence='DL-MRPLDAVE', b_score=1, y_score=2, total_score=3, precursor_distance=0.00045174999991104414, total_mass_error=0.003261479531289524), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='EVMRPLDAVE', hybrid_sequence='EV-MRPLDAVE', b_score=1, y_score=2, total_score=3, precursor_distance=0.00045174999991104414, total_mass_error=0.0032614795313179457), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LDMSWSPILP', hybrid_sequence='LD-MSWSPILP', b_score=1, y_score=2, total_score=3, precursor_distance=0.0015592500000138898, total_mass_error=0.005907827656045583), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DIMSWSPILP', hybrid_sequence='DI-MSWSPILP', b_score=1, y_score=2, total_score=3, precursor_distance=0.0015592500000138898, total_mass_error=0.005907827656045583), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='DLMSWSPILP', hybrid_sequence='DL-MSWSPILP', b_score=1, y_score=2, total_score=3, precursor_distance=0.0015592500000138898, total_mass_error=0.005907827656045583), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='IDMSWSPILP', hybrid_sequence='ID-MSWSPILP', b_score=1, y_score=2, total_score=3, precursor_distance=0.0015592500000138898, total_mass_error=0.005907827656045583), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='VEMSWSPILP', hybrid_sequence='VE-MSWSPILP', b_score=1, y_score=2, total_score=3, precursor_distance=0.0015592500000138898, total_mass_error=0.005907827656074005), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='EVMSWSPILP', hybrid_sequence='EV-MSWSPILP', b_score=1, y_score=2, total_score=3, precursor_distance=0.0015592500000138898, total_mass_error=0.005907827656074005), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='LSEGLTTHGPF', hybrid_sequence='LSEGLTT-HGPF', b_score=2, y_score=2, total_score=3.0, precursor_distance=0.002136749999976928, total_mass_error=0.012619295820286425), HybridSequenceAlignment(left_proteins=[], right_proteins=None, sequence='KCPQPGSEVLT', hybrid_sequence='KCPQ-PGSEVLT', b_score=3, y_score=0, total_score=2.5, precursor_distance=0.00045124999996914994, total_mass_error=0.0037202866797088063)])}


    def test_json_file(self):
        #Test the summary.json_file function
        #Create the json file
        summary.json_file(results, output_dir)
        #Check the summary file exists


    # def test_tsv_file:
    #     #Test the summary.tsv_file function
    
    # def test_generate:
    #     #Test the summary.generate function