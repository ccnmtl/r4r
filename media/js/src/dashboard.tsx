import React, { useEffect, useState } from 'react';
import { toTitleCase } from './utils';
import { useLocation } from 'react-router-dom';

interface DashboardProps {
    children: React.JSX.Element
    detail: string
    title: string
}

export default function Dashboard(
    {children, detail = '', title}: DashboardProps
){
    const location = useLocation();

    const [breadcrumbs, setBreadcrumbs] = useState(
        location.pathname.split('/').slice(4));
    useEffect(() => {
        setBreadcrumbs(location.pathname.split('/').slice(4));
    }, [location]);

    return <section id='dashboard'>
        <ol className='breadcrumb small mb-3'>
            <li className='breadcrumb-item'>{title}</li>
            {breadcrumbs.map((item, i) =>
                <li key={i} className='breadcrumb-item'>
                    {toTitleCase(item)}</li>)}
        </ol>
        <div className={`d-flex align-items-end justify-content-between gap-3 
            flex-wrap`}
        >
            <div className='mb-4'>
                <h1 className='h2 fw-bold mb-1'>{title}</h1>
                {detail.length > 0 &&
                    <p className='text-secondary mb-0'>{detail}</p>}
            </div>
        </div>
        {children}
    </section>;
};