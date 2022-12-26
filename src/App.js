import './App.css';
import L from "leaflet";
import PrimaryBar from './PrimaryBar';

function App() {
  var map = L.map('map',{center:[36.2048,138.2529],zoom:5});
  return (
    <div className="App">
      <PrimaryBar map={map}/>
    </div>
  );
}

export default App;
