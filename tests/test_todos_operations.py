import os
from selene import browser, have, command


# Заполнение и отправка формы

def test_fill_out_and_submit_the_form(setup_browser):
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Bell')
    browser.element('#userEmail').type('alexbell@gmail.com')
    # browser.element('[name=gender][value=Male]+label').click()
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('8999888998')
    browser.element('#dateOfBirthInput').click()
    # browser.element('.react-datepicker__month-select').click()
    # browser.element('.react-datepicker__month-select').element('option[value="3"]').click()
    browser.element('.react-datepicker__month-select').type('April')
    # browser.element('.react-datepicker__year-select').click()
    # browser.element('.react-datepicker__year-select').element('option[value="1992"]').click()
    browser.element('.react-datepicker__year-select').type('1992')
    browser.element('.react-datepicker__day--010').click()
    browser.element('#subjectsInput').perform(command.js.scroll_into_view)
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    # browser.element('label[for=hobbies-checkbox-1]').click()
    browser.all('#hobbiesWrapper .custom-control').element_by(have.exact_text('Sports')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('Picture/picture.jpg'))
    browser.element('#currentAddress').type('110006 Kashmiri Gate')
    browser.element('#state').click()
    # browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    # browser.all("#city div").element_by(have.exact_text("Delhi")).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text("Delhi")).click()
    browser.element('#submit').click()
    # browser.element('#submit').perform(command.js.click)
    browser.element('[id=example-modal-sizes-title-lg]').should(have.text('Thanks for submitting the form'))

    browser.element('.table').all('td').should(have.texts(
        ('Student Name', 'Alex Bell'),
        ('Student Email', 'alexbell@gmail.com'),
        ('Gender', 'Male'),
        ('Mobile', '8999888998'),
        ('Date of Birth', '10 April,1992'),
        ('Subjects', 'Computer Science'),
        ('Hobbies', 'Sports'),
        ('Picture', 'picture.jpg'),
        ('Address', '110006 Kashmiri Gate'),
        ('State and City', 'NCR Delhi'),
    )
    )
