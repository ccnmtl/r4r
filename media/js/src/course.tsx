import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';
import { CaseProps, CourseProps } from './utils';

export default function Course() {
    const [course, setCourse] = useState<CourseProps>();
    const { courseId } = useParams();

    useEffect(() => {
        axios.get(`/api/course/${courseId}/`)
            .then(response => setCourse(response.data));
    }, []);

    const generateCase = (medCase:CaseProps, key:number) =>
        <section key={key} className="card" id={`day${key+1}`}>
            <div className="card-header">
                <h4>{medCase.title}</h4>
            </div>
            <div className="card-body">
                {medCase.days.map((day, key) =>
                    <p key={key}>{day.title}</p>
                )}
            </div>
        </section>;

    return course ?
        <section id='course'>
            <h2>{course.title}</h2>
            <p>{course.code}</p>
            <p>{course.details ||
                <em className='text-secondary'>No details</em>}</p>
            <Link to={'/'}>Return to Course List</Link>
            <section id='rotations' className='row p-2 g-3'>
                {course.rotations.map((rotation, key) =>
                    <section key={key} className='col-xl-4'
                        id={`rotation${key+1}`}
                    >
                        <div className="card text-bg-light">
                            <h3 className='card-header'>
                                {`Rotation ${key+1}: ${rotation.title}`}</h3>
                            <div className='card-body'>
                                {/* 'case' is a protected keyword */}
                                {rotation.cases.length > 0 ?
                                    rotation.cases.map((medCase, key) =>
                                        medCase.days.length > 0 ?
                                            generateCase(medCase, key)
                                            :
                                            <em className='text-secondary'>
                                                No Days</em>)
                                    :
                                    <em className='text-secondary'>
                                        No Cases</em>}
                            </div>
                        </div>
                    </section>
                )}
            </section>
        </section>
        :
        <div className='spinner-border text-secondary' role='status'>
            <span className='visually-hidden'>Loading...</span>
        </div>;
};