import React, { useState } from 'react';
import { Link, Outlet } from 'react-router-dom';
import { toTitleCase } from './utils';


export interface TabProps {
    el: React.JSX.Element
    path: string
}

interface TabListProps {
    tabs: TabProps[]
}

export default function TabList(
    {tabs}: TabListProps
) {
    const [active, setActive] = useState(0);

    return <div className='row g-4 align-items-start mx-0'>
        <ul className='nav nav-tabs'>
            {tabs.map(({path}, i) => {
                const focus = active === i ?
                    'text-bg-primary' :
                    'bg-secondary-subtle text-secondary-emphasis';
                return <li key={i} className='nav-item'>
                    <Link to={path}
                        onClick={() => setActive(i)}
                        className={`nav-link d-flex align-items-center gap-2
                            ${active === i ? 'active fw-semibold' : ''}`}
                    >
                        {toTitleCase(path)}
                        <span className={`badge ${focus}`}>
                            {0}
                        </span>
                    </Link>
                </li>;
            })}
        </ul>
        <Outlet />
    </div>;
}