// .Navigation_bar.js

import React from 'react';
import {
    Nav1,
    NavLink,
    Bars,
    NavMenu,
    NavBtn,
    NavBtnLink,
} from "./css/NavbarElements";

// Functional component
const NavBar = () => {

  return (
    <Nav1>
     <Bars />

	  <NavMenu>
             <NavLink to ="/">Home</NavLink>
             <NavLink to ="/regions">Region</NavLink>
             <NavLink to ="/environments">Environment</NavLink>
	  </NavMenu> 
	  <NavBtn>
	     <NavBtnLink>SignIn</NavBtnLink>
	   </NavBtn>
    </Nav1>
  );
};


export default NavBar;

