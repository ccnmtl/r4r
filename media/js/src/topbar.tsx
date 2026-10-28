import React from 'react';
import { authUser } from './utils';
import { Link } from 'react-router-dom';
import BrandMark from './brandMark';
import CSRFToken from './csrfToken';

const NAV = [
    ['/', 'Dashboard'],
    ['/members', 'Members'],
    ['/rotations', 'Rotations'],
    ['/feedback', 'Feedback'],
    ['/about', 'About eHostpital']
];

const isStaff = authUser.is_staff;

export default function Topbar() {
    return <nav
        className='app-topbar navbar navbar-expand px-3 px-lg-4 text-white'
    >
        <div className='container-fluid gap-3 flex-wrap'>
            <Link to={'/'}
                className={`navbar-brand btn d-flex align-items-center 
                    gap-2 border-0 p-0 text-white`}
            >
                <BrandMark size='sm' />
                <span className='fw-bold'>eHospital</span>
            </Link>
            <ul className='nav nav-pills nav-dark me-auto gap-3'>
                {NAV.map((link, i) => <li key={i} className='nav-item'>
                    <Link className='nav-link' to={link[0]}>{link[1]}</Link>
                </li>)}
            </ul>
            <div className='d-flex align-items-center gap-3'>
                {authUser.is_superuser &&
                    <a href='/_impersonate/list/'
                        title='Impersonate'
                        className='badge bg-alert'
                    >
                        Impersonate
                    </a>
                }
                <span className='badge bg-white text-primary'>
                    {isStaff ? 'Instructor' : 'Student'}
                </span>
                <span className='fw-medium'>{authUser.username}</span>
                <form action='/cas/logout' method='post'>
                    <CSRFToken />
                    <button type='submit'
                        className='nav-link g-4' title='Log Out'
                    >
                        <i className='bi bi-box-arrow-right p-1'></i>
                        <span title='Log Out'>Log Out</span>
                    </button>
                </form>
            </div>
        </div>
    </nav>;
};