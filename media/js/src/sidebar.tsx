import React from 'react';
import { Link, useParams } from 'react-router-dom';
import Avatar from './avatar';
import BrandMark from './brandMark';
import { authUser } from './utils';


export default function Sidebar({unread}) {
    const { courseId } = useParams();
    const PATH = window.location.pathname;
    const base = `/course/${courseId}/`;
    const INSTRUCTOR_NAV = [
        ['Dashboard', base],
        ['Members', base + 'members/'],
        ['Rotation', base + 'rotation/'],
        ['Feedback', base + 'feedback/'],
        ['About eHospital', '/about/'],
    ];
    console.log(authUser);

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
            {INSTRUCTOR_NAV.map(([label, url], i) =>
                <li key={i} className='nav-item'>
                    <Link to={'/'}
                        className={`nav-link w-100 text-start d-flex 
                            align-items-center gap-2 ${url === PATH ?
                                'active fw-semibold' : ''}`}
                    >
                        {label}
                        {url === '/base/feedback/' && unread > 0 &&
                            <span className='badge bg-danger ms-auto'
                                aria-label={unread + ' unread'}>{unread}</span>
                        }
                    </Link>
                </li>
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
                    <button type='submit' title='Sign Out'
                        className='btn btn-link btn-sm p-0 text-white'
                    >
                        <span title='Sign Out'>Sign Out</span>
                    </button>
                </div>
            </div>
        </div>
    </nav>;
};