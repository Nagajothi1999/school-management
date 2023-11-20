$(document).ready(() => {
    const passwordField = $('#id_password1');
    const confirmPasswordField = $('#id_password2');
    const submitButton = $('#register-submit');

    const switchSubmitButton = () => {
        const isEnabled = validatePassword() && validateConfirmPassword()
        console.log({ pw:validatePassword(), cpw: validateConfirmPassword() })
        submitButton.prop('disabled', !isEnabled)
    };

    // Function to create and show error div
    function showError(message) {
        // Remove any existing error div
        $('.password-error').remove();

        // Create and append the error div after the password field
        const errorDiv = $(`
            <div class="password-error">
                <p class="text-danger">
                    <strong>${message}</strong>
                </p>
            </div>
        `);
        passwordField.after(errorDiv);
    }

    // Function to create and show error div
    function showConfirmPasswordError(message) {
        // Remove any existing error div
        $('.confirm-password-error').remove();

        // Create and append the error div after the password field
        const errorDiv = $(`
            <div class="confirm-password-error">
                <p class="text-danger">
                    <strong>${message}</strong>
                </p>
            </div>
        `);
        confirmPasswordField.after(errorDiv);
    }

    // Function to remove error div
    const removeError = () => {
        $('.password-error').remove();
    }

    // Function to remove error div
    const removeConfirmPasswordError = () => {
        $('.confirm-password-error').remove();
    }

    // Function to validate password
    function validatePassword() {
        const password = passwordField.val();
        const isInValidRegex = /^\d+$/.test(password)
        const hasRequiredLength = password.length >= 8
        // Check if the password is too short or entirely numeric
        if (!hasRequiredLength) {
            showError('This password is too short. It must contain at least 8 characters.');
        } else if (isInValidRegex) {
            showError('This password is entirely numeric.');
        } else {
            removeError();
        }
        return hasRequiredLength && !isInValidRegex 
    }

    // Function to validate confirm password
    function validateConfirmPassword() {
        const password = passwordField.val();
        const confirmPassword = confirmPasswordField.val();
        if (password !== confirmPassword) {
            showConfirmPasswordError('The two password fields didn’t match.')
        } else {
            removeConfirmPasswordError()
        }
        return password === confirmPassword
    }

    // Validate on blur
    passwordField.on('blur', () => {
        validatePassword()
        switchSubmitButton()
    });

    // Validate confirm password on blur
    confirmPasswordField.on('blur', () => {
        validateConfirmPassword()
        switchSubmitButton()
    });

    // Validate on change
    passwordField.on('input', removeError);

    // Validate on change
    confirmPasswordField.on('input', removeConfirmPasswordError);
});