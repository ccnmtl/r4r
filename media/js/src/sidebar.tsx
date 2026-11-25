import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';
import Avatar from './avatar';
import BrandMark from './brandMark';
import { authUser } from './utils';
import CSRFToken from './csrfToken';
import axios from 'axios';


export default function Sidebar({unread = 0}) {
    const [rotations, setRotations] = useState([]);
    const [navList, setNavList] = useState([
        ['Feedback', 'feedback'],
        [],
        ['Members', 'members'],
        ['Insights', 'insights'],
        ['About eHospital', 'about'],
    ]);

    const { courseId } = useParams();
    const PATH = window.location.pathname;

    useEffect(() => {
        axios.get(`/api/course/${courseId}/rotations/`)
            .then(response => setRotations(response.data));
    }, []);

    useEffect(() => {
        const nav = [['Feedback', 'feedback']];
        rotations.forEach(item =>
            nav.push([
                `Case: ${item['title']}`, `rotation/${item['id']}`]));
        nav.push(
            ['Members', 'members'],
            ['Insights', 'insights'],
            ['About eHospital', 'about']
        );
        setNavList(nav);
    }, [rotations]);

    return <nav
        className={`app-sidebar d-flex flex-column flex-shrink-0 p-3 sticky-top 
            vh-100 text-white`}
    >
        <Link to={'/'}
            className={`btn d-flex align-items-center gap-2 px-2 border-0 
                text-white`}
        >
            <BrandMark />
            <span className='fs-5 fw-bold'>eHospital</span>
        </Link>
        <div className={`app-sidebar__label fw-semibold text-uppercase px-3 
            pt-4 pb-2`}
        >
            Faculty - {authUser.is_superuser &&
                <a href='/_impersonate/list/'
                    title='Impersonate'
                    className='text-white'
                >
                    Impersonate
                </a>
            }
        </div>
        <ul className="nav nav-pills nav-dark flex-column gap-1">
            {navList.map(([label, url], i) =>
                label ?
                    <li key={i} className='nav-item'>
                        <Link to={`/course/${courseId}/${url}`}
                            className={`nav-link w-100 text-start d-flex 
                                align-items-center gap-2 ${url === PATH ?
                                    'active fw-semibold' : ''}`}
                        >
                            {label}
                            {url === '/base/feedback/' && unread > 0 &&
                                <span className='badge bg-danger ms-auto'
                                    aria-label={unread + ' unread'}
                                >
                                    {unread}
                                </span>
                            }
                        </Link>
                    </li>
                    :
                    <div className='spinner-border mx-3'
                        role='status'
                    >
                        <span className='visually-hidden'>Loading...</span>
                    </div>
            )}
        </ul>
        <div className={`app-sidebar__footer mt-auto d-flex align-items-center 
            gap-2 pt-3`}
        >
            <Avatar text={undefined} size="34"
                className="bg-white text-primary small" />
            <div className="flex-grow-1 min-w-0">
                <div className="small fw-semibold text-truncate">
                    {authUser.first_name} {authUser.last_name}</div>
                <div className="d-flex align-items-center gap-2">
                    <span className="badge bg-white text-primary">Faculty</span>
                    <form action='/cas/logout' method='post'>
                        <CSRFToken />
                        <button type='submit' title='Sign Out'
                            className='btn btn-link btn-sm p-0 text-white'
                        >
                            <span title='Sign Out'>Sign Out</span>
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </nav>;
};