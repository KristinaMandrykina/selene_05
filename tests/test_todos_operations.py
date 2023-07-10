import os

from selene import browser, have


# Заполнение и отправка формы

def test_fill_out_and_submit_the_form(setup_browser):
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Bell')
    browser.element('#userEmail').type('alexbell@gmail.com')
    #browser.element('[name=gender][value=Male]+label').click()
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('89998889988')
    browser.element('#dateOfBirthInput').click()
    #browser.element('.react-datepicker__month-select').click()
    #browser.element('.react-datepicker__month-select').element('option[value="3"]').click()
    browser.element('.react-datepicker__month-select').type('April')
    #browser.element('.react-datepicker__year-select').click()
    #browser.element('.react-datepicker__year-select').element('option[value="1992"]').click()
    browser.element('.react-datepicker__year-select').type('1992')
    browser.element('.react-datepicker__day--0{10}').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    #browser.element('label[for=hobbies-checkbox-1]').click()
    browser.all('#hobbiesWrapper .custom-control').element_by(have.exact_text('Sports')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('Picture/picture.jpg'))
    browser.element('#currentAddress').type('110006 Kashmiri Gate')
    browser.element('#state').click()
    # browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    #browser.all("#city div").element_by(have.exact_text("Delhi")).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text("Delhi")).click()
