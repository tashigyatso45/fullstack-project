import { Container, Stack } from "@chakra-ui/react";
import Navbar from "./component/Navbar";

const App = () => {
  return (
    <Stack minH={"100vh"}>
      <Navbar />
      <Container maxW={"1200px"} my={4}></Container>
    </Stack>
  );
};

export default App;
