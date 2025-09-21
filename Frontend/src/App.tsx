import Upload from "./components/Upload";
import Chat from "./components/Chat";

function App() {
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center text-gray-800 mb-8">Knowledge AI</h1>
      <Upload />
      <Chat />
    </div>
  );
}

export default App;
