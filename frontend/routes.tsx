import { createBrowserRouter } from 'react-router-dom';
import QGenView from "Frontend/views/QGenView";


const router = createBrowserRouter([
  { path: '/', element: <QGenView></QGenView>},
]);
export default router;
