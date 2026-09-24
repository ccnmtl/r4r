import React from 'react';

export default function Contact() {
    // @ts-expect-error: Event data is known
    const handleSubmit = (event) => {
        event.preventDefault();
        const data = event;
        console.log('Form data:', data);
    };


    return <section id='contact-us' className='container'>
        <h1>Contact Us</h1>
        <p>Comments, Questions, and Feedback can be made known below:</p>
        <p>You can reach us at <a href='mailto:ctl-dev@columbia.edu'>
            ctl-dev@columbia.edu</a> or user the form below</p>
        <form onSubmit={handleSubmit}>
            <div className='row g-4'>
                <div className="col-lg-4">
                    <label htmlFor='contact-name' className='form-label'>
                        Name</label>
                    <input type='text' id='contact-name'
                        className='form-control' />
                </div>
                <div className="col-lg-4">
                    <label htmlFor='contact-email' className='form-label'>
                        Email</label>
                    <input type='text' id='contact-email'
                        className='form-control' />
                </div>
                <div className="col-lg-8">
                    <label htmlFor='contact-body' className='form-label'>
                        Message</label>
                    <textarea id='contact-body' className='form-control' />
                </div>
            </div>
            <button type='submit' className='btn btn-primary mt-4'>
                Submit</button>
        </form>
    </section>;
};