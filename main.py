from pyscript import document

def eligibility_computation(event):

    # Registration 
    reg_yes = document.getElementById("reg_yes").checked
    reg_no = document.getElementById("reg_no").checked

    # Medical clearance
    clear_yes = document.getElementById("clear_yes").checked
    clear_no = document.getElementById("clear_no").checked

    # Dropdown
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    # Grade and Section
    valid_grades = ["seven", "eight", "nine", "ten"]
    valid_sections = ["eme", "ruby", "sapph", "top"]

    result = document.getElementById("result")

    # eligibility
    if reg_yes:
        if clear_yes:
            if grade in valid_grades:

                if section == "eme":
                    result.innerHTML = "<p class='text-success'>Congrats! You're in the Green Hornets! </p>"

                elif section == "ruby":
                    result.innerHTML = "<p class='text-success'>Congrats! You're in the Red Bulldogs!</p>"

                elif section == "sapph":
                    result.innerHTML = "<p class='text-success'>Congrats! You're in the Blue Bears!</p>"

                elif section == "top":
                    result.innerHTML = "<p class='text-success'>Congrats! You're in the Yellow Tigers!</p>"

            else:
                result.innerHTML = "<p class='text-danger'>Not Eligible.</p>"

        else:
            result.innerHTML = "<p class='text-danger'>Not Eligible. Make sure to get medical clearance first!</p>"

    else:
        result.innerHTML = "<p class='text-danger'>Not Eligible. Make sure to register first!</p>"

