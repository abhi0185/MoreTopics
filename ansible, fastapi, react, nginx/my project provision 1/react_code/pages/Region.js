import React, { useState, useEffect } from 'react';
import styles from '../my-style.module.css';
import Heading from '../components/Heading';
import NavBar from '../components/Navigation_bar';
import RegionNav from '../components/Region_nav';

const Region = () => {
  const [regions, setRegions] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http:///172.21.200.115:5000/regions');
        if (!response.ok) {
          console.error('error 1')
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('data  : ', data);
        setRegions(data.Regions);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <Heading />
      <NavBar />
      <RegionNav />

      <h2 className={styles.bigblue}>Regions</h2>
      <table>
        <thead>
          <tr>
            <th>Code</th>
            <th>Name</th>
            <th>Description</th>
            <th>Create Date</th>
            <th>Active</th>
          </tr>
        </thead>
          <tbody>
            {regions.length > 0 ? (
               regions.map(region => (
            <tr key={region.code}>
             <td>{region.code}</td>
             <td>{region.name}</td>
             <td>{region.description}</td>
             <td>{region.create_date}</td>
             <td>{region.is_active ? 'Yes' : 'No'}</td>
            </tr>
        ))
  ) : (
    <tr>
      <td colSpan="5">Loading...</td>
    </tr>
  )}
</tbody>

	  </table>
    </div>
  );
};

export default Region;

