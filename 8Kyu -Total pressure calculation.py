def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    # your code goes here
    molar_mass1 = given_mass1 * 0.001/molar_mass1
    molar_mass2 = given_mass2 * 0.001/molar_mass2
    temp = temp + 273.15
    gas_constant = 0.082
    return (((molar_mass1 + molar_mass2) * gas_constant * temp) / volume) * 1000
