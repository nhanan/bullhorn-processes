///// FIELD INTERACTIONS /////

///// If category = 2000009 then make customTextBlock6 required
var categories = API.getActiveValue();
var hasMatch = categories.some(category => category.id === 2000009 || category === 2000009);

API.setRequired('customTextBlock6', hasMatch && API.form.value.customText29?.trim());




///// This code validates emails checking it again the format of *@*.*
// Retrieve the value of the currently active field
var activeValue = API.getActiveValue();

// Check if the active value is empty or if it matches the email format using a regular expression
if (activeValue === "" || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(activeValue)) {
    // If the active value is empty or it matches the email format, do nothing (considered valid).
} else {
    // If the active value does not match the email format, mark it as invalid with a specific error message.
    API.markAsInvalid(API.getActiveKey(), "Invalid Email Format");
}




///// This code validates phone numbers to ensure they have at least 6 digits and not 5 of the same number consecutively
// Retrieve the value of the currently active field
var activeValue = API.getActiveValue();

// Regular expression to find 5 consecutive same digits
var repeatingDigitsRegex = /(\d)\1{4}/;

// Check if the active value is empty or if it contains at least 6 digits
if (activeValue === "" || (activeValue.length >= 6 && !repeatingDigitsRegex.test(activeValue))) {

} else {
    API.markAsInvalid(API.getActiveKey(), "Invalid Phone Number");
}




///// This code ensures 2 x skills are added per Candidate
var activeValue = API.getActiveValue();

// Check if activeValue has 2 or more elements, or is empty
if (activeValue.length >= 2 || activeValue.length === 0) {
} else {
    API.markAsInvalid(API.getActiveKey(), activeValue);
}





///// Toast to remind Consultants to update CA/DM record
var activeValue = API.getActiveValue();
if (activeValue === "CA Qualification") {
    API.displayToast({
        title: 'Update Record',
        message: "Please check all mandatory fields are updated on the record.",
        theme: "danger",
        hideDelay: 10000,
    });
}




///// PAGE INTERACTIONS /////
