import React from "react";
import { Button, Text, View } from "react-native";
import { DrawerNavigationProp } from "@react-navigation/drawer";

const Home: React.FC<{ navigation: DrawerNavigationProp<any> }> = (
  navigation
) => {
  return (
    <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
      <Text> Home </Text>
      <Button
        onPress={() => navigation.navigate("Notifications")}
        title="Go to notifications"
      />
    </View>
  );
};

export default Home;
