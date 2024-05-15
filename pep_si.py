import math

print("Design of Elastomeric Leveling Pad (PEP) - Method A")
print("by: Abdul Rochim\n")
print("Calculation Finish")
print("For report, see the txt file.\n")

file_pep = open("report_pep.txt", "w")
file_pep.writelines("--------------------------------------------------------------------\n")
file_pep.writelines("                                                                    \n")
file_pep.writelines("                   ELASTOMERIC LEVELING PAD (PEP)                   \n")
file_pep.writelines("                      coprights : Abdul Rochim                      \n")
file_pep.writelines("                                                                    \n")
file_pep.writelines("--------------------------------------------------------------------\n\n")

#Material and Section Properties
#Leveling Pad Dimensions
W = 939.8 #mm Leveling Pad Width
L = 254 #mm Leveling Pad Length
hri = 19.05 #mm Leveling Pad Thickness
hrt = hri

#Leveling Pad Material Properties
Duro = 60 #(min)

#Shear Modulus
type_prop = "Shore A"
G = 0.896 #MPa

#Bridge Geometry
grade_betweensupport = -1.50 #%
Ad = 381 #mm bearing to FF Abutment


#Bearing Rotations
tetha_d = 0.004 #rad
tetha_r = 0.005 #rad

#Bearing Loads
#Service I Limit State
DL = 604.93 #kN

file_pep.writelines(["MATERIAL AND SECTION PROPERTIES\n"])
file_pep.writelines(["   Leveling Pad Dimensions\n"])
file_pep.writelines(["   Leveling Pad Width,       W = ", str(W), " mm\n"])
file_pep.writelines(["   Leveling Pad Length,      L = ", str(L), " mm\n"])
file_pep.writelines(["   Leveling Pad Thickness, hri = ", str(hri), " mm\n\n"])
file_pep.writelines(["   Leveling Pad Material Properties\n"])
file_pep.writelines(["   ",type_prop, " Durometer Hardness\n\n"])

file_pep.writelines(["Shear Modulus\n"])
file_pep.writelines(["   The least favorable value is assumed since the material is spesified by its hardness value (AASHTO 14.7.6.2)\n"])

file_pep.writelines(["   G = {0:0.2f}".format(G), " MPa\n"])
if G < 1.724 and G > 0.5516:
    file_pep.writelines(["   Check, 0.5516 MPa < G < 1.724 MPa  [ OK ]\n\n"])
else:
    file_pep.writelines(["   Check, G < 0.5516 MPa or G > 1.724 MPa  [ OK ]\n\n"])

file_pep.writelines(["BRIDGE GEOMETRY\n"])
file_pep.writelines(["   Profile grade between supports (%) = {0:0.2f}".format(grade_betweensupport), " %\n"])
file_pep.writelines(["   bearing to FF Abutment,         Ad = {0:0.2f}".format(Ad), " mm\n\n"])

file_pep.writelines(["BEARING ROTATIONS\n"])
file_pep.writelines(["   Rotations include effects of girder camber. For all rotation value, positive indicates an upward rotation while negative indicates a downward rotation.\n"])
file_pep.writelines(["   Service I Limit State Loads\n"])
file_pep.writelines(["   Net girder rotations (camber plus dead loads), tetha_d = {0:0.3f}".format(tetha_d), " rad\n\n"])

file_pep.writelines(["   include a rotational allowance of 0.005 radians due to uncertainties in bearing facrication and bearing seats. Per BDM 14.5.4, the flatness tolerance for bearing seat uncertainties in accounted for in the rotational allowance.\n"])
file_pep.writelines(["   Construction Tolerance, tetha_r = {0:0.3f}".format(tetha_r), " rad\n\n"])

file_pep.writelines(["BEARING LOADS\n"])
file_pep.writelines(["   Loads acting on the leveling pad are dead load girder reactions, up to and including the deck pour, at the service limit state.\n"])

file_pep.writelines(["   Service I Limit State\n"])
file_pep.writelines(["   DL = {0:0.2f}".format(DL), " kN\n\n"]) 

#SOLUTION
#Shape Factor
Si = L * W / (2. * hri * ( L + W ))

#Compressive Stress
stress_s = DL * 1000./ (L * W)

#Compressive Deflection
dho_d_req = 0.09 * hri
stress_d = DL * 1000./ (L * W)
epsilon_d = stress_d / (4.8 * G * Si**2.0)
dho_d = epsilon_d * hri

#Stability
L_req = L/3.0
W_req = W/3.0
min_req_L_and_W = min(L_req, W_req)

#Geometry
tetha_max = -1. * math.atan((hrt - dho_d)/ Ad)
tetha_grade = math.atan(grade_betweensupport/100.)
tetha_total = tetha_d - tetha_r + tetha_grade

file_pep.writelines(["SOLUTION\n"])
file_pep.writelines(["1. Shape Factor\n"])
file_pep.writelines(["   Total thickness of interior layer, hri, is equel to total elastomer thickness, hrt (hri = hrt)\n"])
file_pep.writelines(["   Rectangular, plan bearing shape factor without holes:\n"])
file_pep.writelines(["   Si = L * W / (2. * hri * ( L + W )\n"])
file_pep.writelines(["      = {0:0.2f}".format(Si), "\n\n"]) 

file_pep.writelines(["2. Compressive state\n"])
file_pep.writelines(["   The compressive stress of the leveling pad shall satisfy the criteria below for a PEP.\n"])
file_pep.writelines(["   stress_s = average compressive due to total load dom applicable service load combinations\n"])
file_pep.writelines(["   stress_s_req_1 = 1.00 G Si = {0:0.2f}".format(1.00 * G * Si), " MPa\n"])
file_pep.writelines(["   stress_s_req_2 = 5.5158 MPa\n"])

file_pep.writelines(["   stress_s = DL/ (LW) = {0:0.2f}".format(stress_s), " MPa\n"])
if stress_s <= 1. * G * Si :
    file_pep.writelines(["   Check, stress_s <= 1.00 GSi,  {0:0.2f}".format(stress_s), " MPa  <  {0:0.2f}".format(1.0 * G * Si), " MPa   [ OK ]\n"])
else :
    file_pep.writelines(["   Check, stress_s > 1.00 G Si   [ OK ]\n\n"])

if stress_s <= 5.5158 :
    file_pep.writelines(["   Check, stress_s <= 5.5158 MPa,  {0:0.2f}".format(stress_s), " MPa  <  {0:0.4f}".format(5.5158), " MPa   [ OK ]\n\n"])
else:
    file_pep.writelines(["   Check, stress_s > 5.5158 MPa   [ NOT OK ]\n\n"])

file_pep.writelines(["3. Compressive Deflection\n"])
file_pep.writelines(["   Compressive deflection under initila dead load of a PEP shall meet the following criteria in AASHTO 14.7.6.3.3 and 14.7.5.3.6.\n"])
file_pep.writelines(["   Total thickness of interior layer, hri, is equal to total elastomer thickness, hrt (hri=hrt).\n"])
file_pep.writelines(["   dho_d <= 0.09 hri = {0:0.3f}".format(dho_d_req), " mm.\n"])
file_pep.writelines(["   stress_d = DL / (LW)\n"])
file_pep.writelines(["   stress_d = {0:0.3f}".format(stress_d), " MPa\n"])
file_pep.writelines(["   epsilon_d = stress_d / (4.8 * G * Si^2)\n"])
file_pep.writelines(["   epsilon_d = {0:0.3f}\n".format(epsilon_d)])
file_pep.writelines(["   dho_d = sigma(epsilon_d * hri)\n"])
file_pep.writelines(["   dho_d = {0:0.3f}".format(dho_d), " mm\n"])
if dho_d < dho_d_req:
    file_pep.writelines(["   dho_d = {0:0.3f}".format(dho_d), " mm  <  {0:0.3f}".format(dho_d_req), " mm  [ OK ]\n\n"]) 
else:
    file_pep.writelines(["   dho_d = {0:0.3f}".format(dho_d), " mm  >  {0:0.3f}".format(dho_d_req), " mm  [ NOT OK ]\n\n"]) 

file_pep.writelines(["4. Stability\n"])
file_pep.writelines(["   Total thickness of interior, hri, is equal to total elastomer thickness, hrt (hri = hrt)\n"])
file_pep.writelines(["   Total bearing thickness shall not exceed the lesser of the following dimensions.\n"])
file_pep.writelines(["   L/3 = {0:0.2f}".format(L_req), " mm\n"])
file_pep.writelines(["   W/3 = {0:0.2f}".format(W_req), " mm\n"])
file_pep.writelines(["   lesser between L/3 and W/3 = {0:0.2f}".format(min_req_L_and_W), " mm\n"])

if hrt < min_req_L_and_W :
    file_pep.writelines(["   Check: hrt = {0:0.2f}".format(hrt), " mm  < {0:0.2f}".format(min_req_L_and_W), " mm   [ OK ]\n\n"])
else:
    file_pep.writelines(["   Check: hrt = {0:0.2f}".format(hrt), " mm  > {0:0.2f".format(min_req_L_and_W), " mm   [ NOT OK ]\n\n"])

file_pep.writelines(["5. Geometry\n"])
file_pep.writelines(["   Confirm that the hickness of the leveling pad is adequate to prevent girder-to-support contact under anticipates girder rotations and roadway geometry. Assume rotations are about the centerline of bearing.\n"])
file_pep.writelines(["   Maximum rotation, including compressive deflection effect, before bottom of girder comes in contact with the top of support:\n"])
file_pep.writelines(["   tetha_max = -tan((hrt-dho_d)/Ad)^(-1) = {0:0.4f}".format(tetha_max), " rad\n"])
file_pep.writelines(["   Rotation of girder due to profile grade of bridge between supports in question:\n"])
file_pep.writelines(["   tetha_grade = tan(%/100) = {0:0.4f}".format(tetha_grade), " rad\n"])
file_pep.writelines(["   Total girder rotation, including camber, dead loads, allowances for construction and bearing fabrication uncertainties, and roadway geometry.\n"])
file_pep.writelines(["   tetha_total = tetha_d - tetha_r + tetha_grade = {0:0.4f}".format(tetha_total), " rad\n"])
file_pep.writelines(["   Total rotations through the deck pour need to be less than the maximum rotation:\n"])

if math.fabs(tetha_max) >= math.fabs(tetha_total) :
    file_pep.writelines(["   tetha_max >= tetha_total ,   {0:0.4f}".format(tetha_max), " rad >= {0:0.4f}".format(tetha_total), " rad  [ OK ]\n"])
else:
    file_pep.writelines(["   tetha_max < tetha_total ,   {0:0.4f}".format(tetha_max), " rad > {0:0.4f}".format(tetha_total), " rad  [ NOT OK ]\n"])


file_pep.close()

