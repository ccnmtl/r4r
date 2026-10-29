import React from 'react';

const CSRF = window.r4r.csrf;

export default function CSRFToken() {
    return <input type="hidden" name="csrfmiddlewaretoken" value={CSRF} />;
};