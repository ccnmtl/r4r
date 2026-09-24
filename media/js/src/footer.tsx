import React from 'react';
import { Link } from 'react-router-dom';


export default function Footer() {
    return <footer className='bg-light text-dark pt-2 pb-5'>
        <ul className='nav d-flex justify-content-center'>
            <li className='nav-item'>
                <Link className='nav-link' to='/about' title='About'>
                    About</Link>
            </li>
            <li className='nav-item'>
                <Link className='nav-link' to='#' title='Help'>Help</Link>
            </li>
            <li className='nav-item'>
                <Link className='nav-link' to='/contact' title='Contact'>
                    Contact</Link>
            </li>
        </ul>

        <span itemScope itemType='http://schema.org/EducationalOrganization'>
            <div className='text-center'>
                <a href='https://ctl.columbia.edu' target='_blank'
                    itemProp='url' title='Center for Teaching and Learning at \
                        Columbia University' className='d-inline-block'>
                    <img src={`${window.r4r.staticUrl}img/logo-ctl-color.png`}
                        className='mx-auto d-block mt-3' alt='' itemProp='logo'
                        width='290' />
                    <span className='visually-hidden' itemProp='name'>
                        Center for Teaching and Learning at Columbia University
                    </span>
                </a>
            </div>
        </span>

    </footer>;
};