package Serialize_Desirialize;

import com.google.gson.*;

import java.lang.reflect.Type;

public class CarSerializer implements Comparable<CarSerializer>, JsonSerializer<Car>, JsonDeserializer<Car> {
    private String Company;
    private String Owner;
    private int id;
    private int Year;

    public CarSerializer() {
        this.id = -1;
        this.Year = 0;
        this.Company = "";
        this.Owner = "";
    }


    public String getCompany() {
        return Company;
    }

    public void setCompany(String company) {
        Company = company;
    }

    public String getOwner() {
        return Owner;
    }

    public void setOwner(String owner) {
        Owner = owner;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getYear() {
        return Year;
    }

    public void setYear(int year) {
        Year = year;
    }

    public CarSerializer(String company, String owner, int id, int year) {
        Company = company;
        Owner = owner;
        this.id = id;
        this.Year = year;
    }

    @Override
    public Car deserialize(JsonElement jsonElement, Type type, JsonDeserializationContext jsonDeserializationContext) throws JsonParseException {
        JsonObject obj = jsonElement.getAsJsonObject();
        System.out.println("h");
        return new Car(obj.get("Company").getAsString(), obj.get("Owner").getAsString(), obj.get("id").getAsInt(), obj.get("Year").getAsInt());
    }

    @Override
    public JsonElement serialize(Car car, Type type, JsonSerializationContext jsonSerializationContext) {
        JsonObject obj = new JsonObject();
        obj.addProperty("Company", this.Company);
        obj.addProperty("Owner", this.Owner);
        obj.addProperty("id", this.id);
        obj.addProperty("Year", this.Year);
        return obj;
    }

    @Override
    public String toString() {
        return "{ \"Company\": " + this.Company + ", \"Owner\": " + this.Owner + ", \"id\": " + this.id + ", \"Year\": " + this.Year + "}";
    }

    @Override
    public int compareTo(CarSerializer o) {
        return this.id - o.id;
    }

}
