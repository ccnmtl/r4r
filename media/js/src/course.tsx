import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';
import { CourseProps } from './utils';


export default function Course() {
    const [course, setCourse] = useState<CourseProps>();
    const { courseId } = useParams();

    useEffect(() => {
        axios.get(`/api/course/${courseId}/`)
            .then(response => setCourse(response.data));
    }, []);

    return <>
        {course ?
            <section id='course'>
                <h2>{course.title}</h2>
                <p>{course.code}</p>
                <p>{course.details ||
                    <em className='text-secondary'>No details</em>}</p>
                <Link to={'/'}>Return to Course List</Link>
            </section>
            :
            <div className='spinner-border text-secondary' role='status'>
                <span className='visually-hidden'>Loading...</span>
            </div>}
    </>;
};