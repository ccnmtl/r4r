import React from 'react';
import { RouteItem } from './utils';


const generateCards = (cards: RouteItem[]) => cards.map(({path, el}, i) =>
    <li key={i} className='card'>
        <div className='card-body p-4'>
            <div className={'h5 card-title card-title--accent text-primary'}>
                {path}</div>
            <div className='card-text mb-0'>{el}</div>
        </div>
    </li>
);

const cards = [
    {path: 'Mission', el: <>Give every intern a structured, well-supported
        rotation, and give faculty a clear view of how their interns are
        progressing.</>},
    {path: 'How it works', el: <>Faculty build a sequence of prompts, each with
        a file, link, round or quiz attached. Students work through the prompts
        in order, and faculty review the resulting feedback by thread, intern
        or keyword.</>},
    {path: 'Contact', el: <>Questions or access requests:
        <a href='mailto:bs2886@cumc.columbia.edu' className='mx-1'>
            bs2886@cumc.columbia.edu</a></>}
];

export default function About() {
    return <section id='about'
        className='container-fluid px-4 px-lg-5 py-4 py-lg-5'
    >
        <ol className='breadcrumb small mb-3'>
            <li className='breadcrumb-item'>About eHostpital</li>
        </ol>
        <div className={`d-flex align-items-end justify-content-between gap-3 
            flex-wrap`}
        >
            <div className='mb-4 col-md-10'>
                <h1 className='h2 fw-bold mb-3'>About eHostpital</h1>
                <p className='lead mb-4'>
                    eHospital is an education platform for clinical training.
                    Faculty organize interns into teams, build rotations from
                    a sequence of prompts and supporting media, and review the
                    feedback interns share along the way.
                </p>
                <ul className='d-flex flex-column gap-3 p-0'>
                    {generateCards(cards)}
                </ul>
            </div>
        </div>
    </section>;
};